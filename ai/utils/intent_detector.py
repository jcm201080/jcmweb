import logging

logger = logging.getLogger(__name__)


def detectar_intencion(pregunta: str) -> str | None:
    """
    Detecta la intención del usuario según palabras clave.
    """

    texto = pregunta.lower()

    # Juegos
    if any(p in texto for p in [
        "jugar", "game", "juego", "bingo",
        "diversión", "entretenimiento", "play", "games"
    ]):
        return "juegos"

    # ERP / backend
    if any(p in texto for p in [
        "backend", "flask", "api", "empresa",
        "erp", "negocio", "gestión", "stock",
        "productos", "ventas"
    ]):
        return "erp"

    # Ciberseguridad
    if any(p in texto for p in [
        "seguridad", "ciber", "logs",
        "ataque", "hacker", "malware",
        "vulnerabilidad"
    ]):
        return "ciber"

    # Contacto / trabajo
    if any(p in texto for p in [
        "trabajo", "contratar", "proyecto",
        "presupuesto", "servicio",
        "colaborar"
    ]):
        return "contacto"

    return None