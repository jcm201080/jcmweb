🌐 JCMWEB – Personal Portfolio (Flask Version)

Professional portfolio website of Jesús Castaño, Python Backend Developer specialized in Flask, Big Data and real-world production deployments.

🔗 Live site: https://jesuscmweb.com

🚀 Overview

JCMWEB is a bilingual (Spanish / English) portfolio application built with Flask, designed to showcase:

Backend systems deployed in VPS environments

Real-world Flask applications

Data analysis & log processing engines

Real-time systems using Socket.IO

Frontend evolution and structured UI projects

The project follows a clean MVC-like structure using Flask routing and modular templates.

🛠 Tech Stack
Backend

Python 3.12

Flask

Jinja2 templating

Modular routing

VPS Deployment

Frontend

HTML5

CSS3 (modular architecture)

JavaScript (vanilla)

Responsive design

Font Awesome

jQuery

Showcased Technologies

Flask Blueprints

SQLAlchemy

Socket.IO

Chart.js

Matplotlib

Log analysis engines

Linux VPS deployment

📁 Project Structure
jcmweb/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── perfil.html
│   ├── proyectos-web.html
│   │
│   ├── en/
│   │   ├── index-en.html
│   │   ├── perfil-en.html
│   │   ├── proyectos-web-en.html
│   │
│   └── partials/
│       ├── header.html
│       ├── footer.html
│       └── hero.html
│
├── static/
│   ├── css/
│   ├── js/
│   ├── img/
│   └── fonts/
│
└── venv/
🌍 Language System

The application supports bilingual navigation using Flask routing:

Spanish → /

English → /en

Language is controlled server-side via route handling and template variables (lang).

No automatic browser redirection is used — language switching is handled manually through navigation.

🎯 Key Features

Featured backend project showcase

Modular CSS architecture

Modal-based project detail system

Bilingual navigation system

Clean Flask routing structure

Responsive design

VPS production deployment

GitHub integration

External project linking

🖥 Run Locally

Clone repository:

git clone https://github.com/jcm201080/jcmweb.git
cd jcmweb

Create virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run application:

python app.py

Open in browser:

http://127.0.0.1:5000
📦 Deployment

The site is deployed on a production VPS environment.

Deployment stack includes:

Linux server

Gunicorn

Nginx reverse proxy

HTTPS (SSL)

📌 Future Improvements

Internationalization system (Flask-Babel)

JS consolidation into ES modules

Performance optimization (Lighthouse 95+ target)

Image compression optimization

Accessibility improvements (WCAG compliance)

SEO structured data implementation

👤 Author

Jesús Castaño
Python Backend Developer

GitHub: https://github.com/jcm201080

LinkedIn: https://www.linkedin.com/in/jesus-castano-822408361

📄 License

This project is for personal portfolio and professional showcase purposes.
