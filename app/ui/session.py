"""
conversation_service.py

Responsabilidad:
    Gestionar el historial de conversación.
"""

from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
)

import streamlit as st

def initialize_conversation() -> None:
    """
    Inicializa el historial de conversación.
    """

    if "messages" not in st.session_state:

        st.session_state.messages = []


def get_conversation_history() -> list[
    BaseMessage
]:
    """
    Obtiene el historial de conversación.
    """

    return st.session_state.messages

def add_user_message(
    question: str,
) -> None:
    """
    Agrega un mensaje del usuario.
    """

    st.session_state.messages.append(
        HumanMessage(
            content=question
        )
    )

def add_ai_message(
    answer: str,
) -> None:
    """
    Agrega la respuesta del asistente.
    """

    st.session_state.messages.append(
        AIMessage(
            content=answer
        )
    )

def clear_conversation() -> None:
    """
    Limpia el historial de conversación.
    """

    st.session_state.messages = []