"""
chatbot_prompt.py

Define el prompt principal utilizado por el chatbot.
"""

from langchain_core.prompts import PromptTemplate


def get_chat_prompt() -> PromptTemplate:
    """
    Crea y devuelve el prompt principal del chatbot.

    Returns:
        PromptTemplate configurado para generar respuestas.
    """

    return PromptTemplate(
        input_variables=["mensaje", "historial"],
        template="""
Eres un asistente útil y amigable llamado ChatBot Pro.

Historial de conversación:
{historial}

Responde de manera clara y concisa a la siguiente pregunta:

{mensaje}
"""
    )