"""
chat_service.py

Responsabilidad:
    Gestionar la comunicación con la cadena de LangChain.
"""
from collections.abc import Iterator
from langchain_core.messages import BaseMessage
import logging
from langsmith import traceable

logger = logging.getLogger(__name__)


@traceable(
    name="Chat Response"
)
def stream_chat_response(
    chain,
    question: str,    
    history: list[BaseMessage],
) -> Iterator[str]:
    """
    Genera una respuesta utilizando streaming.

    Args:
        chain: Cadena LCEL.
        question: Pregunta realizada por el usuario.
        history: Historial de conversación.

    Yields:
        Fragmentos de texto generados por el modelo.
    """
    logger.info(
        "Generando respuesta..."
    )
    for chunk in chain.stream(
        {
            "mensaje": question,
            "historial": history,
        }
    ):
        yield chunk