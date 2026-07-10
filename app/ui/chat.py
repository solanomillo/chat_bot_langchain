from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    SystemMessage,
)
from app.services.chat_service import stream_chat_response
import streamlit as st

from app.ui.session import (
    add_ai_message, 
    add_user_message,
    get_conversation_history
)


def render_chat_history(
    messages: list[BaseMessage],
) -> None:
    """
    Renderiza el historial del chat.

    Args:
        messages: Historial de conversación.
    """

    for message in messages:

        if isinstance(message, SystemMessage):
            continue

        role = (
            "assistant"
            if isinstance(message, AIMessage)
            else "user"
        )

        with st.chat_message(role):
            st.markdown(message.content)




def handle_chat(
    chain,
) -> None:
    """
    Gestiona la conversación con el usuario.

    Args:
        chain: Cadena principal del chatbot.
    """

    question = st.chat_input(
        "Escribe tu mensaje..."
    )

    if not question:
        return

    with st.chat_message("user"):
        st.markdown(question)

    full_response = ""

    with st.chat_message("assistant"):

        placeholder = st.empty()

        for chunk in stream_chat_response(
            chain=chain,
            question=question,
            history=get_conversation_history(),
        ):

            full_response += chunk

            placeholder.markdown(
                full_response + "▌"
            )

        placeholder.markdown(full_response)

    add_user_message(question)

    add_ai_message(full_response)