import requests
import logging

logger = logging.getLogger(__name__)

def cargar_readme(url):

    try:
        r = requests.get(url, timeout=5)

        if r.status_code == 200:
            return r.text[:4000]  # limitar tamaño
        else:
            logger.warning("No se pudo cargar README")
            return ""

    except Exception as e:
        logger.error(f"Error leyendo README: {e}")
        return ""