"""
llm_service.py

Responsabilidad:
    Crear y configurar el modelo de lenguaje.
"""

from langchain_openai import ChatOpenAI

from app.config.settings import (
    API_KEY_DEEPSEEK,
    BASE_URL,
    DEFAULT_REASONING_EFFORT,
    THINKING_CONFIG
)
import logging

logger = logging.getLogger(__name__)


def create_chat_model(
    model_name: str,
    temperature: float,
) -> ChatOpenAI:
    """
    Crea una instancia configurada del modelo de lenguaje.

    Args:
        model_name: Nombre del modelo seleccionado.
        temperature: Nivel de creatividad del modelo.

    Returns:
        Instancia configurada de ChatOpenAI.
    """
    logger.info(
        "Inicializando modelo %s",
        model_name,
    )
    return ChatOpenAI(
        model=model_name,
        api_key=API_KEY_DEEPSEEK,
        base_url=BASE_URL,
        temperature=temperature,
        reasoning_effort=DEFAULT_REASONING_EFFORT,
        extra_body=THINKING_CONFIG
    )