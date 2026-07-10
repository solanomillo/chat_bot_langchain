<div align="center">

# 🤖 Basic ChatBot

**Chatbot conversacional construido con LangChain, Streamlit y DeepSeek, diseñado con una arquitectura modular, buenas prácticas de ingeniería de software y observabilidad mediante LangSmith.**

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-1.x-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit)
![DeepSeek](https://img.shields.io/badge/LLM-DeepSeek-purple)
![LangSmith](https://img.shields.io/badge/LangSmith-Tracing-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

</div>

---

# 📖 Descripción

Basic ChatBot es una aplicación conversacional desarrollada con **LangChain** y **Streamlit** que permite interactuar con modelos de lenguaje compatibles con la API de OpenAI (DeepSeek en este proyecto).

El objetivo principal no fue únicamente construir un chatbot funcional, sino desarrollar una aplicación siguiendo principios de arquitectura limpia, separación de responsabilidades y buenas prácticas utilizadas en proyectos profesionales de IA.

---

# ✨ Características

- 💬 Chat conversacional con historial
- ⚡ Respuestas en tiempo real mediante Streaming
- 🤖 Selección dinámica del modelo
- 🌡 Configuración de temperatura desde la interfaz
- 🧩 Arquitectura modular
- 📝 Prompt desacoplado de la aplicación
- 🔍 Observabilidad con LangSmith
- 📋 Logging centralizado
- ⚠ Manejo de excepciones específicas
- 📚 Código documentado con Docstrings y Type Hints

---

# 🏛 Arquitectura

```
Usuario
      │
      ▼
 Streamlit UI
      │
      ▼
 Chat Service
      │
      ▼
 Chat Chain (LCEL)
      │
      ▼
 ChatOpenAI (DeepSeek)
      │
      ▼
 DeepSeek API
```

La aplicación sigue una arquitectura por capas donde cada módulo tiene una única responsabilidad.

---

# 📂 Estructura del proyecto

```text
app/
│
├── chains/
│   └── chat_chain.py
│
├── config/
│   └── settings.py
│
├── prompts/
│   └── chatbot_prompt.py
│
├── services/
│   ├── chat_service.py
│   ├── llm_service.py
│   └── langsmith_service.py
│
├── ui/
│   ├── chat.py
│   ├── page.py
│   ├── session.py
│   └── sidebar.py
│
├── utils/
│   └── logger.py
│
└── app.py
```

---

# 🧠 Arquitectura aplicada

Durante el desarrollo se aplicaron principios de ingeniería de software como:

- Single Responsibility Principle (SRP)
- Separación de responsabilidades
- Bajo acoplamiento (Low Coupling)
- Alta cohesión (High Cohesion)
- Código autoexplicativo
- Configuración centralizada
- Modularización
- Observabilidad
- Streaming de respuestas mediante LCEL

---

# 🛠 Tecnologías

| Tecnología | Uso |
|------------|-----|
| Python 3.13 | Lenguaje principal |
| LangChain | Orquestación del LLM |
| Streamlit | Interfaz web |
| DeepSeek | Modelo de lenguaje |
| LangSmith | Observabilidad |
| Python Logging | Registro de eventos |
| python-dotenv | Variables de entorno |

---

# 🚀 Instalación

## 1. Clonar el repositorio

```bash
https://github.com/solanomillo/chat_bot_langchain.git

cd chat_bot_langchain
```

---

## 2. Crear entorno virtual

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# ⚙ Variables de entorno

Crear un archivo `.env`

```env
API_KEY_DEEPSEEK=

LANGSMITH_API_KEY=

LANGSMITH_TRACING=true

LANGSMITH_PROJECT=basic-chatbot
```

---

# ▶ Ejecutar la aplicación

```bash
streamlit run app.py
```

---

# 🖥 Interfaz

Aquí puedes colocar capturas de pantalla o un GIF del funcionamiento.

```
images/

chat.png

sidebar.png

demo.gif
```

---

# 🔍 Observabilidad

El proyecto incorpora **LangSmith** para registrar automáticamente:

- Prompt enviado
- Historial de conversación
- Modelo utilizado
- Tiempo de ejecución
- Tokens consumidos
- Errores
- Trazabilidad completa de la ejecución

---

# 📋 Logging

La aplicación utiliza el módulo estándar `logging` de Python para registrar:

- Inicio de la aplicación
- Inicialización del modelo
- Inicio de conversación
- Generación de respuestas
- Manejo de errores
- Eventos importantes

---

# ⚠ Manejo de errores

Se implementó manejo específico para:

- AuthenticationError
- APIConnectionError
- APITimeoutError
- RateLimitError
- Excepciones inesperadas

Esto permite ofrecer mensajes amigables al usuario mientras los detalles técnicos quedan registrados en los logs.

---

# 📈 Flujo de ejecución

```
Usuario

↓

Interfaz Streamlit

↓

Sidebar

↓

Configuración del modelo

↓

Prompt

↓

Cadena LCEL

↓

DeepSeek

↓

Streaming

↓

Respuesta
```

---

# 🧪 Próximas mejoras

- [ ] Docker
- [ ] Tests unitarios
- [ ] Persistencia de conversaciones
- [ ] Multi Provider (OpenAI, Gemini, Cohere)
- [ ] Exportar conversaciones
- [ ] RAG
- [ ] LangGraph
- [ ] Docker Compose

---

# 📚 Aprendizajes

Este proyecto permitió reforzar conocimientos sobre:

- Arquitectura modular
- LangChain Expression Language (LCEL)
- Streaming de respuestas
- Observabilidad con LangSmith
- Logging profesional
- Manejo de excepciones
- Organización de proyectos Python
- Configuración centralizada
- Buenas prácticas de desarrollo

---

# 🤝 Contribuciones

Las contribuciones son bienvenidas.

Si encuentras algún problema o tienes una mejora, puedes abrir un Issue o enviar un Pull Request.

---

# 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT.

---

<div align="center">

Desarrollado con ❤️ utilizando **Python**, **LangChain** y **Streamlit**

</div>
