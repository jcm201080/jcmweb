import os
from db import db, Visita
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
from config import Config
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

ADMIN_EMAIL = app.config["ADMIN_EMAIL"]
ADMIN_PASSWORD = app.config["ADMIN_PASSWORD"]



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

# -------------------------
# CONTROL DE VISITAS
# -------------------------

@app.before_request
def registrar_visita():
    if session.get("admin"):
        return

    if request.method != "GET":
        return

    if request.path.startswith("/static"):
        return

    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ip and "," in ip:
        ip = ip.split(",")[0].strip()

    nueva_visita = Visita(
        ip=ip,
        user_agent=request.headers.get("User-Agent"),
        ruta=request.path,
        fecha=datetime.utcnow()
    )

    db.session.add(nueva_visita)
    db.session.commit()
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


from sqlalchemy import func

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
    ).group_by(Visita.ruta).order_by(func.count(Visita.id).desc()).limit(5).all()

    return render_template(
        "admin_visitas.html",
        total_visitas=total_visitas,
        visitas_unicas=visitas_unicas,
        visitas_hoy=visitas_hoy,
        top_rutas=top_rutas
    )




# -------------------------
# RUN
# -------------------------

if __name__ == "__main__":
    app.run(debug=True)