import logging

logger = logging.getLogger(__name__)


PROJECT_KEYWORDS = {
    
    "juegos": [
        "game", "games", "play", "real time", "realtime",
        "websocket", "multiplayer", "interactive"
    ],

    "erp": [
        "business", "store", "shop", "inventory",
        "management", "sales", "stock", "database"
    ],

    "ciber": [
        "security", "cyber", "logs", "monitoring",
        "analysis", "dashboard", "attack", "threat"
    ],

    "burger": [
        "restaurant", "food", "burger", "menu",
        "business website", "local business"
    ]
}


def recomendar_proyecto(texto):

    texto = texto.lower()

    for proyecto, keywords in PROJECT_KEYWORDS.items():
        if any(k in texto for k in keywords):
            logger.info(f"🎯 Proyecto recomendado: {proyecto}")
            return proyecto

    return None