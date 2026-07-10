import streamlit as st

from app.chains.chat_chains import create_chat_chain
from app.prompts.chatbot_prompt import get_chat_prompt
from app.ui.session import initialize_conversation
from app.services.llm_service import create_chat_model
from app.utils.logger import configure_logger
from app.ui.chat import (
    handle_chat,
    render_chat_history,
)

from app.ui.page import configure_page
from app.ui.sidebar import render_sidebar



def main() -> None:
    """
    Punto de entrada de la aplicación.
    """
    configure_logger()
    configure_page()

    initialize_conversation()

    model_name, temperature = render_sidebar()

    chat_prompt = get_chat_prompt()

    chat_model = create_chat_model(
        model_name=model_name,
        temperature=temperature,
    )

    chat_chain = create_chat_chain(
        prompt=chat_prompt,
        llm=chat_model,
    )

    render_chat_history(
        st.session_state.messages
    )

    handle_chat(chat_chain)


if __name__ == "__main__":
    main()