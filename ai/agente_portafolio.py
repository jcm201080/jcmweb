import os
from litellm import completion
from .contexto_portafolio import contexto_portafolio

import os
print("GROQ KEY:", os.getenv("GROQ_API_KEY"))


# Modelos que intentará usar el agente
MODELOS_GROQ = [
    "groq/llama-3.3-70b-versatile",
    "groq/llama3-70b-8192",
    "groq/mixtral-8x7b-32768"
]


def detectar_intencion(pregunta: str):
    """
    Detecta intención básica del usuario para recomendar proyectos.
    """

    texto = pregunta.lower()

    if any(p in texto for p in ["jugar", "game", "juego", "bingo"]):
        return "juegos"

    if any(p in texto for p in ["backend", "flask", "api", "empresa", "erp"]):
        return "erp"

    if any(p in texto for p in ["seguridad", "ciber", "logs", "ataque"]):
        return "ciber"

    if any(p in texto for p in ["trabajo", "contratar", "proyecto", "presupuesto"]):
        return "contacto"

    return None


def respuesta_intencion(intencion):
    """
    Respuestas rápidas sin usar IA.
    """

    if intencion == "juegos":
        return (
            "Si quieres probar algo interactivo te recomiendo la **Plataforma Juegos JCM**.\n\n"
            "Es una aplicación desarrollada con Flask y Socket.IO con sistemas en tiempo real.\n\n"
            "Puedes probarla aquí:\n"
            "https://juegos.jesuscmweb.com"
        )

    if intencion == "erp":
        return (
            "Si te interesa ver un proyecto backend completo te recomiendo el "
            "**Sistema de Gestión Empresarial (ERP)**.\n\n"
            "Incluye autenticación de usuarios, gestión de productos, stock, ventas "
            "y dashboards de datos.\n\n"
            "Proyecto:\n"
            "https://informatica.jesuscmweb.com"
        )

    if intencion == "ciber":
        return (
            "Puedes ver el proyecto de **Análisis de Logs de Ciberseguridad**.\n\n"
            "Este sistema analiza logs de servidores para detectar IPs sospechosas "
            "y patrones de ataque.\n\n"
            "Proyecto:\n"
            "https://ciberseguridad.jesuscmweb.com"
        )

    if intencion == "contacto":
        return (
            "Jesús Castaño desarrolla proyectos backend con Flask, APIs, "
            "sistemas en tiempo real y análisis de datos.\n\n"
            "Si tienes una idea o proyecto puedes contactar desde la sección "
            "de contacto del portafolio:\n\n"
            "https://jesuscmweb.com/contacto"
        )

    return None


def preguntar_portafolio(pregunta: str):
    """
    Función principal del agente IA.
    """

    # 1️⃣ detectar intención
    intencion = detectar_intencion(pregunta)

    if intencion:
        respuesta = respuesta_intencion(intencion)
        if respuesta:
            return respuesta

    # 2️⃣ si no hay intención clara → usar IA
    for modelo in MODELOS_GROQ:

        try:
            response = completion(
                model=modelo,
                messages=[
                    {"role": "system", "content": contexto_portafolio},
                    {"role": "user", "content": pregunta}
                ],
                temperature=0.3
            )

            return response["choices"][0]["message"]["content"]

        except Exception as e:
            print(f"Error con modelo {modelo}: {e}")
            continue

    return "Lo siento, el asistente no está disponible en este momento."