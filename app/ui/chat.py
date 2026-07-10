"""
chat.py

Responsabilidad:
    Renderizar el historial del chat y gestionar la conversación.
"""

import logging

import streamlit as st
from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    SystemMessage,
)
from openai import (
    APIConnectionError,
    APITimeoutError,
    AuthenticationError,
    RateLimitError,
)

from app.services.chat_service import stream_chat_response
from app.ui.session import (
    add_ai_message,
    add_user_message,
    get_conversation_history,
)

logger = logging.getLogger(__name__)


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


def handle_chat(chain) -> None:
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

        try:

            logger.info("Generating response.")

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

            logger.info("Response generated successfully.")

        except AuthenticationError:

            logger.exception("Authentication failed.")

            st.error(
                "❌ La API Key configurada no es válida."
            )

        except RateLimitError:

            logger.warning("Rate limit exceeded.")

            st.warning(
                "⚠️ Se alcanzó el límite de solicitudes. Inténtalo nuevamente en unos segundos."
            )

        except APIConnectionError:

            logger.exception("Unable to connect to the API.")

            st.error(
                "🌐 No fue posible conectar con el proveedor de IA."
            )

        except APITimeoutError:

            logger.exception("Request timeout.")

            st.warning(
                "⏳ El modelo tardó demasiado en responder."
            )

        except Exception:

            logger.exception("Unexpected error while generating response.")

            st.error(
                "❌ Ocurrió un error inesperado."
            )