print("APP FILE:", __file__)
import os
from db import db, Visita
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from functools import wraps
from dotenv import load_dotenv
from datetime import timedelta
from sqlalchemy import func

from ai.orchestrator.orchestrator import preguntar_orchestrator

import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev_secret_key")

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL",
    "sqlite:////var/www/jcmweb_flask/instance/visitas.db"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Verificar permisos de escritura en la BD
DB_PATH = os.path.join(BASE_DIR, "instance", "visitas.db")

if not os.access(DB_PATH, os.W_OK):
    logging.warning(f"La base de datos no tiene permisos de escritura: {DB_PATH}")

ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")



db.init_app(app)

with app.app_context():
    db.create_all()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("admin"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


from flask import g

# -------------------------
# CONTROL DE VISITAS
# -------------------------
@app.after_request
def registrar_visita(response):

    if session.get("admin"):
        return response

    if request.path.startswith("/static"):
        return response

    if request.path == "/favicon.ico":
        return response
    
    user_agent = request.headers.get("User-Agent", "").lower()

    if "bot" in user_agent or "crawler" in user_agent or "spider" in user_agent:
        return response

    ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    if ip and "," in ip:
        ip = ip.split(",")[0].strip()

    visita = Visita(
        ip=ip,
        user_agent=request.headers.get("User-Agent"),
        ruta=request.path,
        metodo=request.method,
        status_code=response.status_code,
        fecha=datetime.utcnow()
    )

    try:
        db.session.add(visita)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        logging.error(f"ERROR GUARDANDO VISITA: {e}")
    finally:
        db.session.remove()

    return response
# -------------------------
# Versión para js, css, imágenes, etc. (sin registro de visitas)
# -------------------------
@app.context_processor
def inject_version():
    return {"static_version": int(datetime.utcnow().timestamp())}
# -------------------------
# ROUTES - ESPAÑOL
# -------------------------

@app.route("/")
def index():
    return render_template("index.html", lang="es")


@app.route("/perfil")
def perfil():
    return render_template("perfil.html", lang="es")


@app.route("/proyectos-web")
def proyectos_web():
    return render_template("proyectos-web.html", lang="es")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Credenciales incorrectas")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

# MOtoGP2026!
@app.route("/motogp")
@login_required
def motogp():
    return render_template("motogp.html")

# -------------------------
# ROUTES - ENGLISH
# -------------------------

@app.route("/en")
def index_en():
    return render_template("en/index-en.html", lang="en")


@app.route("/en/perfil")
def perfil_en():
    return render_template("en/perfil-en.html", lang="en")


@app.route("/en/projects")
def proyectos_web_en():
    return render_template("en/proyectos-web-en.html", lang="en")

@app.route("/gracias")
def gracias():
    return render_template("gracias.html", lang="es")


@app.route("/en/thanks")
def thanks_en():
    return render_template("en/gracias-en.html", lang="en")




@app.route("/admin/visitas")
@login_required
def admin_visitas():
    total_visitas = Visita.query.count()

    visitas_unicas = db.session.query(
        Visita.ip
    ).distinct().count()

    visitas_hoy = db.session.query(func.count(Visita.id)).filter(
        func.date(Visita.fecha) == func.current_date()
    ).scalar()

    top_rutas = db.session.query(
        Visita.ruta,
        func.count(Visita.id).label("total")
    ).group_by(Visita.ruta)\
     .order_by(func.count(Visita.id).desc())\
     .limit(5).all()

    # 📊 VISITAS ÚLTIMOS 7 DÍAS (con días vacíos en 0)
    hoy = datetime.utcnow().date()
    dias = [hoy - timedelta(days=i) for i in range(6, -1, -1)]

    resultado = db.session.query(
        func.date(Visita.fecha).label("dia"),
        func.count(Visita.id)
    ).filter(
        Visita.fecha >= datetime.utcnow() - timedelta(days=7)
    ).group_by("dia").all()

    # Convertimos a diccionario {fecha: total}
    visitas_dict = {str(r[0]): r[1] for r in resultado}

    fechas = []
    totales = []

    for dia in dias:
        fechas.append(dia.strftime("%d-%m"))
        totales.append(visitas_dict.get(str(dia), 0))

    # 🔥 TOP IPs
    top_ips = db.session.query(
        Visita.ip,
        func.count(Visita.id).label("total")
    ).group_by(
        Visita.ip
    ).order_by(
        func.count(Visita.id).desc()
    ).limit(10).all()

    # 🚨 TOP 404
    top_404 = db.session.query(
        Visita.ruta,
        func.count(Visita.id).label("total")
    ).filter(
        Visita.status_code == 404
    ).group_by(
        Visita.ruta
    ).order_by(
        func.count(Visita.id).desc()
    ).limit(10).all()

    # ⏰ VISITAS POR HORA (0-23)
    resultado_horas = db.session.query(
        func.strftime('%H', Visita.fecha),
        func.count(Visita.id)
    ).group_by(
        func.strftime('%H', Visita.fecha)
    ).all()

    horas_dict = {int(r[0]): r[1] for r in resultado_horas if r[0] is not None}

    horas_labels = list(range(24))
    horas_totales = [horas_dict.get(h, 0) for h in horas_labels]

    # 📅 VISITAS POR DÍA DE LA SEMANA
    resultado_dias = db.session.query(
        func.strftime('%w', Visita.fecha),
        func.count(Visita.id)
    ).group_by(
        func.strftime('%w', Visita.fecha)
    ).all()

    dias_dict = {int(r[0]): r[1] for r in resultado_dias if r[0] is not None}

    dias_labels = ["Dom", "Lun", "Mar", "Mie", "Jue", "Vie", "Sab"]
    dias_totales = [dias_dict.get(i, 0) for i in range(7)]


    # 📅 VISITAS POR MES
    resultado_meses = db.session.query(
        func.strftime('%m', Visita.fecha),
        func.count(Visita.id)
    ).group_by(
        func.strftime('%m', Visita.fecha)
    ).all()

    meses_dict = {int(r[0]): r[1] for r in resultado_meses if r[0] is not None}

    meses_labels = [
        "Ene","Feb","Mar","Abr","May","Jun",
        "Jul","Ago","Sep","Oct","Nov","Dic"
    ]

    meses_totales = [meses_dict.get(i+1, 0) for i in range(12)]

    return render_template(
        "admin_visitas.html",
        total_visitas=total_visitas,
        visitas_unicas=visitas_unicas,
        visitas_hoy=visitas_hoy,
        top_rutas=top_rutas,
        fechas=fechas,
        totales=totales,
        top_ips=top_ips,
        top_404=top_404,
        horas_labels=horas_labels,
        horas_totales=horas_totales,
        dias_labels=dias_labels,
        dias_totales=dias_totales,
        meses_labels=meses_labels,
        meses_totales=meses_totales
    )

#----------------
# Agente Ia
#---------

@app.route("/api/portafolio_ai", methods=["POST"])
def portafolio_ai():

    data = request.json
    pregunta = data.get("pregunta", "")

    if not pregunta:
        return jsonify({"respuesta": "No he recibido ninguna pregunta."})

    respuesta = preguntar_orchestrator(pregunta)

    return jsonify({"respuesta": respuesta})

# -------------------------
# RUN
# -------------------------

if __name__ == "__main__":
    app.run(debug=True)