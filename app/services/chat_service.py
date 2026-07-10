"""
chat_service.py

Responsabilidad:
    Gestionar la comunicación con la cadena de LangChain.
"""
from collections.abc import Iterator
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import BaseMessage



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
    
    for chunk in chain.stream(
        {
            "mensaje": question,
            "historial": history,
        }
    ):
        yield chunk