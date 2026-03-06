# /var/www/jcmweb_flask/ai/agente_portafolio.py

"""
Wrapper para el agente del portfolio.
Mantiene compatibilidad con el código existente.
"""

from .agente_router import preguntar_portafolio as preguntar_portafolio_router

# Re-exportamos la función del router
preguntar_portafolio = preguntar_portafolio_router

# También podemos exportar otras funciones si son necesarias
__all__ = ['preguntar_portafolio']