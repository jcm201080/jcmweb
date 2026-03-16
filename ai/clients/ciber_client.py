import requests
import logging

logger = logging.getLogger(__name__)

CIBER_AGENT_URL = "https://ciberseguridad.jesuscmweb.com/ai/ask"


def consultar_agente_ciber(pregunta: str):

    try:
        response = requests.post(
            CIBER_AGENT_URL,
            json={"pregunta": pregunta},
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            return data.get("respuesta")

    except Exception as e:
        logger.error(f"Error consultando agente ciber: {e}")

    return None