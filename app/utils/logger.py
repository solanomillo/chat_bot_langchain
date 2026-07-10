"""
logger.py

Responsabilidad:
    Configurar el sistema de logging de la aplicación.
"""

import logging


def configure_logger() -> None:
    """
    Configura el sistema de logging.
    """

    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        ),
    )