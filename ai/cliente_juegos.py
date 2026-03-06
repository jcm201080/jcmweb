# /var/www/jcmweb_flask/ai/cliente_juegos.py

import requests
import logging
from typing import Optional

logger = logging.getLogger(__name__)

# Configuración - AJUSTA SEGÚN TU ENTORNO
JUEGOS_API_URL = "http://localhost:5001"  # Puerto donde corre la app de juegos
JUEGOS_ENDPOINT = f"{JUEGOS_API_URL}/api/agente-portfolio"  # Endpoint específico
TIMEOUT_SEGUNDOS = 5  # Un poco más de tiempo para que el agente piense

def consultar_agente_juegos(pregunta: str) -> Optional[str]:
    """
    Consulta al agente de la plataforma de juegos.
    """
    try:
        logger.info(f"🔍 Consultando agente de juegos: {pregunta[:50]}...")
        
        response = requests.post(
            JUEGOS_ENDPOINT,
            json={"pregunta": pregunta},
            timeout=TIMEOUT_SEGUNDOS,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            data = response.json()
            respuesta = data.get('respuesta', '')
            fuente = data.get('fuente', 'desconocida')
            
            logger.info(f"✅ Respuesta recibida del agente de juegos (fuente: {fuente})")
            return respuesta
        else:
            logger.warning(f"⚠️ Respuesta inesperada: {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        logger.error("❌ No se pudo conectar con el agente de juegos")
        return None
    except requests.exceptions.Timeout:
        logger.error(f"❌ Timeout al consultar agente de juegos ({TIMEOUT_SEGUNDOS}s)")
        return None
    except Exception as e:
        logger.error(f"❌ Error inesperado: {str(e)}")
        return None

# Función para probar la conexión
def probar_conexion_juegos() -> bool:
    """
    Prueba si el agente de juegos está accesible
    """
    try:
        response = requests.get(
            f"{JUEGOS_API_URL}/api/agente-portfolio/test",
            timeout=3
        )
        return response.status_code == 200
    except:
        return False