"""
sidebar.py

Responsabilidad:
    Renderizar la barra lateral de configuración.
"""

import streamlit as st
from app.config.settings import (
    AVAILABLE_MODELS,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
)
from app.ui.session import (
    clear_conversation,
)
import logging

logger = logging.getLogger(__name__)


def render_sidebar() -> tuple[str, float]:
    """
    Renderiza la barra lateral.

    Returns:
        tuple[str, float]:
            Modelo seleccionado y temperatura.
    """

    with st.sidebar:

        st.header("⚙️ Configuración")

        temperature = st.slider(
            "Temperatura",
            min_value=0.0,
            max_value=1.0,
            value=DEFAULT_TEMPERATURE,
            step=0.1,
            help="Controla la creatividad del modelo.",
        )

        model_name = st.selectbox(
            "Modelo",
            AVAILABLE_MODELS,
            index=AVAILABLE_MODELS.index(DEFAULT_MODEL),
        )

        st.divider()

        st.caption("⚡ Configuración actual")

        st.caption(f"Modelo: {model_name}")

        st.caption(f"Temperatura: {temperature}")

        if st.button(
            "🧾 Nuevo chat",
            use_container_width=True,
        ): 
            clear_conversation()
            st.rerun()
            
        logger.info(
            "Nueva conversación iniciada."
        )
    return model_name, temperature