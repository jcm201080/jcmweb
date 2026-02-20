from flask import Flask, render_template
import os

app = Flask(__name__)

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


# -------------------------
# RUN
# -------------------------

if __name__ == "__main__":
    app.run(debug=True)