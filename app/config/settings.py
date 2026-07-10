"""
settings.py

Configuración centralizada de la aplicación.
"""

import os

from dotenv import load_dotenv

load_dotenv()

# ==========================
# API
# ==========================

API_KEY_DEEPSEEK = os.getenv("API_KEY_DEEPSEEK")

BASE_URL = "https://api.deepseek.com"

# ==========================
# Modelos
# ==========================

DEFAULT_MODEL = "deepseek-v4-flash"

AVAILABLE_MODELS = [
    "deepseek-v4-flash",
    "deepseek-v4-pro",
]

DEFAULT_TEMPERATURE = 0.5

DEFAULT_REASONING_EFFORT = "medium"

PAGE_TITLE = "ChatBot"
PAGE_ICON = "🤖"