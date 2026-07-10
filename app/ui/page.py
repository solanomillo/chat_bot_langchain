"""
page.py

Responsabilidad:
    Configurar la página principal de la aplicación Streamlit.
"""

import streamlit as st
from app.config.settings import PAGE_ICON, PAGE_TITLE
import logging

logger = logging.getLogger(__name__)


def configure_page() -> None:
    """
    Configura la página principal de Streamlit.
    """
    logger.info(
        "Aplicación iniciada."
    )
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
    )

    st.title(f"{PAGE_ICON} {PAGE_TITLE}")

    st.markdown(
        """
        Bienvenido al ChatBot.

        Este es un chatbot construido con LangChain y Streamlit.
        Puedes hacer preguntas y recibir respuestas generadas por un modelo de lenguaje.
        """
    )