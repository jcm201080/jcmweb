import logging
from litellm import completion

logger = logging.getLogger(__name__)


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


def traducir_a_ingles(texto: str) -> str:

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