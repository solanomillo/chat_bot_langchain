from app.config.settings import (
    API_KEY_DEEPSEEK,
    BASE_URL,
    AVAILABLE_MODELS,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    DEFAULT_REASONING_EFFORT,
)

from app.prompts.chatbot_prompt import get_chat_prompt
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import streamlit as st



# configurar la pagina de la app

st.set_page_config(page_title="ChatBot", page_icon="🤖")
st.title("🤖 ChatBot")
st.markdown("Bienvenido al ChatBot! Este es un chatbot simple construido con Streamlit y LangChain. Puedes hacer preguntas y recibir respuestas generadas por el modelo de lenguaje.")


with st.sidebar:
    st.header("⚙️ Configuración")
    
    # Temperatura
    temperature = st.slider(
        "Temperatura", 
        min_value=0.0, 
        max_value=1.0, 
        value=DEFAULT_TEMPERATURE,  # Valor por defecto del ejemplo original
        step=0.1,
        help="Controla la creatividad de las respuestas. Valores más altos = más creativo"
    )
    
    # Modelo
    model_name = st.selectbox(
        "Modelo", 
        AVAILABLE_MODELS,
        index=0,  # Por defecto selecciona el primero
        help="Selecciona el modelo de lenguaje a utilizar"
    )
    
    
    # Mostrar la configuración actual
    st.divider()
    st.caption(f"⚡ Configuración actual:")
    st.caption(f"• Temperatura: {temperature}")
    st.caption(f"• Modelo: {model_name}")
    
    # Crear el modelo de chat con la configuración seleccionada
    chat_model = ChatOpenAI(
    model=model_name,
    api_key=API_KEY_DEEPSEEK,
    base_url=BASE_URL,
    temperature=temperature,
    reasoning_effort=DEFAULT_REASONING_EFFORT,
    extra_body={
            "thinking": {
                "type": "enabled"
            }
        } 
    )

   
    if st.button('🧾Nuevo chat', use_container_width=True):
        st.session_state.mensajes = []
        st.rerun()





# Iniciar el historial de mensajes
if 'mensajes' not in st.session_state:
    st.session_state.mensajes = []
    
prompt_template = get_chat_prompt()
    
# crear cadena usando LCEL
cadena = prompt_template | chat_model
    
# Mostrar el mensaje en la interfaz
for msg in st.session_state.mensajes:
    if isinstance(msg, SystemMessage):
        # No muestra el mensaje por pantalla
        continue
    
    role = 'assistant' if isinstance(msg, AIMessage) else 'user'
    with st.chat_message(role):
        st.markdown(msg.content)
      

# cuadro de texto para que el usuario escriba su mensaje
pregunta = st.chat_input("Escribe tu mensaje aquí...")

if pregunta:
    # Mostrar el menasaje de usuario en la interfaz
    with st.chat_message("user"):
        st.markdown(pregunta)
    
    try:
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""
 
            # ¡Aquí está la magia del streaming!
            for chunk in cadena.stream({"mensaje": pregunta, "historial": st.session_state.mensajes}):
                full_response += chunk.content
                response_placeholder.markdown(full_response + "▌")  # El cursor parpadeante
            
            response_placeholder.markdown(full_response)
        
        # No olvides almacenar los mensajes
        st.session_state.mensajes.append(HumanMessage(content=pregunta))
        st.session_state.mensajes.append(AIMessage(content=full_response))
        
    except Exception as e:
        # ¿Qué tipo de errores podrían ocurrir aquí?
        st.error(f"Error al generar respuesta: {str(e)}")
        st.info("Verifica que tu API Key de OpenAI esté configurada correctamente.")

    