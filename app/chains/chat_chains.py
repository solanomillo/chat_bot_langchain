"""
chat_chain.py

Responsabilidad:
    Construir la cadena principal del chatbot.
"""

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable


def create_chat_chain(
    prompt,
    llm,
) -> Runnable:
    """
    Construye la cadena principal del chatbot.

    Args:
        prompt: Prompt principal.
        llm: Modelo de lenguaje.

    Returns:
        Cadena LCEL configurada.
    """

    return (
        prompt
        | llm
        | StrOutputParser()
    )