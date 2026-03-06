# ai/orchestrator/orchestrator.py

import logging
from ..agents.portfolio_agent import portfolio_agent

logger = logging.getLogger(__name__)


def preguntar_orchestrator(pregunta, historial=None):
    """
    Orquestador principal de agentes IA.
    Decide qué agente debe responder.
    """

    logger.info("🧠 AI Orchestrator activo")

    # De momento todo se envía al agente portfolio
    logger.info("➡️ Orchestrator → Portfolio Agent")

    return portfolio_agent(pregunta, historial)