# /var/www/jcmweb_flask/ai/agente_router.py

import os
import random
import logging
from litellm import completion
from .contexto_portafolio import contexto_portafolio
from .cliente_juegos import consultar_agente_juegos  # ✅ Import correcto

logger = logging.getLogger(__name__)

# Variables de entorno
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Modelos que intentará usar el agente
MODELOS_GROQ = [
    "groq/llama-3.3-70b-versatile",
    "groq/llama3-70b-8192",
    "groq/mixtral-8x7b-32768"
]

# Variaciones para respuestas de intención (más naturales)
RESPUESTAS_VARIADAS = {
    "juegos": [
        "¡Claro! Si buscas diversión interactiva, te recomiendo la **Plataforma Juegos JCM**. Está desarrollada con Flask y Socket.IO para ofrecer experiencias en tiempo real. Puedes probarla aquí: https://juegos.jesuscmweb.com",
        
        "Me encanta que preguntes por la parte lúdica! La plataforma de juegos usa WebSockets para crear sistemas en tiempo real. Échale un vistazo: https://juegos.jesuscmweb.com",
        
        "¿Quieres jugar? La plataforma de juegos tiene sistemas interactivos con tecnología de tiempo real. Está hecha con Flask y Socket.IO. Pruébala: https://juegos.jesuscmweb.com"
    ],
    
    "erp": [
        "El proyecto ERP es perfecto si quieres ver un backend completo. Incluye gestión de productos, stock, ventas y dashboards. Todo con Flask y SQLAlchemy: https://informatica.jesuscmweb.com",
        
        "El Sistema de Gestión Empresarial es uno de los proyectos más completos. Tiene autenticación, control de stock y gráficas interactivas. Míralo aquí: https://informatica.jesuscmweb.com",
        
        "¿Te interesa la gestión empresarial? El ERP desarrollado con Flask incluye productos, clientes, proveedores y dashboards con Chart.js: https://informatica.jesuscmweb.com"
    ],
    
    "ciber": [
        "El sistema de análisis de logs detecta IPs sospechosas y patrones de ataque usando Pandas. Muy útil para ciberseguridad: https://ciberseguridad.jesuscmweb.com",
        
        "Si te interesa la seguridad, este proyecto analiza logs de servidores para identificar comportamientos anómalos y posibles ataques: https://ciberseguridad.jesuscmweb.com",
        
        "Procesamiento de logs con Python y Pandas para detectar amenazas. Así funciona el proyecto de ciberseguridad: https://ciberseguridad.jesuscmweb.com"
    ],
    
    "contacto": [
        "¿Tienes un proyecto en mente? Jesús desarrolla aplicaciones Flask, APIs, sistemas en tiempo real y análisis de datos. Puedes contactar desde: https://jesuscmweb.com/contacto",
        
        "Para presupuestos o consultoría, lo mejor es contactar directamente desde el portfolio: https://jesuscmweb.com/contacto. Jesús está especializado en backend Python.",
        
        "Si necesitas desarrollar algo con Flask, procesamiento de datos o sistemas en tiempo real, escríbele desde: https://jesuscmweb.com/contacto"
    ]
}

def detectar_intencion(pregunta: str):
    """
    Detecta intención básica del usuario para recomendar proyectos.
    Versión mejorada con más palabras clave.
    """
    texto = pregunta.lower()
    
    # Intención juegos
    if any(p in texto for p in ["jugar", "game", "juego", "bingo", "diversión", "entretenimiento", "jugabilidad", "gam", "play"]):
        return "juegos"
    
    # Intención ERP / backend
    if any(p in texto for p in ["backend", "flask", "api", "empresa", "erp", "negocio", "gestión", "stock", "productos", "ventas", "comercial"]):
        return "erp"
    
    # Intención ciberseguridad
    if any(p in texto for p in ["seguridad", "ciber", "logs", "ataque", "hacker", "vulnerabilidad", "firewall", "intrusión", "malware"]):
        return "ciber"
    
    # Intención contacto / servicios
    if any(p in texto for p in ["trabajo", "contratar", "proyecto", "presupuesto", "servicio", "desarrollar", "contratación", "precio", "colaborar"]):
        return "contacto"
    
    return None

def detectar_idioma(texto: str) -> str:

    texto = texto.lower()

    palabras_en = [
        "hello","hi","hey",
        "what","how","where","when","why",
        "game","games","play","available",
        "project","projects","developer",
        "there","can","you","tell","about"
    ]

    if any(p in texto for p in palabras_en):
        return "en"

    return "es"
def respuesta_intencion(intencion):
    """
    Respuestas variadas según la intención detectada.
    """
    if intencion in RESPUESTAS_VARIADAS:
        return random.choice(RESPUESTAS_VARIADAS[intencion])
    
    return None

def traducir_a_ingles(texto):
    try:
        response = completion(
            model="groq/llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "Translate the following text to English. Only return the translated text."
                },
                {
                    "role": "user",
                    "content": texto
                }
            ],
            temperature=0
        )

        return response["choices"][0]["message"]["content"]

    except Exception as e:
        logger.error(f"Error traduciendo: {e}")
        return texto

def preguntar_portafolio(pregunta: str, historial=None):
    """
    Función principal del agente IA con memoria de conversación.
    """
    logger.info(f"📝 Pregunta recibida: {pregunta[:100]}...")
    idioma = detectar_idioma(pregunta)
    logger.info(f"🌍 Idioma detectado: {idioma}")
    
    # Inicializar historial si no existe
    if historial is None:
        historial = []
    
    # 1️⃣ Detectar intención
    intencion = detectar_intencion(pregunta)
    logger.info(f"🎯 Intención detectada: {intencion}")
    
    # 🎮 CASO ESPECIAL: Juegos - Consultar al agente especializado
    if intencion == "juegos":
        logger.info("🔄 Consultando agente de juegos...")
        
        # Intentar obtener respuesta del agente de juegos
        respuesta_juegos = consultar_agente_juegos(pregunta)

        if respuesta_juegos:
            logger.info("✅ Respuesta recibida del agente de juegos")

            # 🌍 Si el usuario habla en inglés → traducir la respuesta
            if idioma == "en":
                respuesta_juegos = traducir_a_ingles(respuesta_juegos)

            # Guardar en historial
            historial.append({"role": "user", "content": pregunta})
            historial.append({"role": "assistant", "content": respuesta_juegos})

            return respuesta_juegos
        else:
            logger.warning("⚠️ Agente de juegos no disponible, usando respaldo")
            # Usar respuesta local de respaldo
            respuesta_local = respuesta_intencion("juegos")

            # Si el idioma es inglés, usar respuesta en inglés
            if idioma == "en":
                respuesta_local = (
                    "You can try the **Juegos JCM platform**, which includes several "
                    "interactive games built with Flask and real-time WebSockets.\n\n"
                    "Try it here: https://juegos.jesuscmweb.com"
                )

            if respuesta_local:
                historial.append({"role": "user", "content": pregunta})
                historial.append({"role": "assistant", "content": respuesta_local})
                return respuesta_local
    
    # 2️⃣ Si hay otra intención clara, responder con variaciones
    if intencion and intencion != "juegos":
        respuesta = respuesta_intencion(intencion)
        if respuesta:
            historial.append({"role": "user", "content": pregunta})
            historial.append({"role": "assistant", "content": respuesta})
            return respuesta
    
    # 3️⃣ Si no hay intención clara, usar IA con Groq
    logger.info("🤔 Usando IA de Groq para responder...")
    
    # Instrucción de idioma
    if idioma == "en":
        instruccion_idioma = "Respond in English."
    else:
        instruccion_idioma = "Responde en español."

    messages = [{
        "role": "system",
        "content": contexto_portafolio + "\n\n" + instruccion_idioma
    }]
    
    # Añadir historial (últimas 3 interacciones)
    for msg in historial[-3:]:
        messages.append(msg)
    
    # Añadir pregunta actual
    messages.append({"role": "user", "content": pregunta})
    
    # Probar modelos
    for modelo in MODELOS_GROQ:
        try:
            response = completion(
                model=modelo,
                messages=messages,
                temperature=0.7,
                max_tokens=300
            )
            
            respuesta_ia = response["choices"][0]["message"]["content"]
            
            # Guardar en historial
            historial.append({"role": "user", "content": pregunta})
            historial.append({"role": "assistant", "content": respuesta_ia})
            
            logger.info(f"✅ Respuesta generada con {modelo}")
            return respuesta_ia
            
        except Exception as e:
            logger.error(f"❌ Error con modelo {modelo}: {e}")
            continue
    
    if idioma == "en":
        return "Sorry, the assistant is temporarily unavailable. Please try again later."
    else:
        return "Lo siento, el asistente no está disponible en este momento. Por favor, intenta más tarde."