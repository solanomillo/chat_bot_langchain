from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
import streamlit as st
import os


load_dotenv()
api_key = os.getenv('API_KEY_DEEPSEEK')

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
        value=0.5,  # Valor por defecto del ejemplo original
        step=0.1,
        help="Controla la creatividad de las respuestas. Valores más altos = más creativo"
    )
    
    # Modelo
    model_name = st.selectbox(
        "Modelo", 
        ["deepseek-v4-flash", "deepseek-v4-pro"],
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
    api_key=api_key,
    base_url="https://api.deepseek.com",
    temperature=temperature,
    reasoning_effort="medium",
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
    
prompt_template = PromptTemplate(
    input_variables=["mensaje", "historial"],
    template="""Eres un asistente útil y amigable llamado ChatBot Pro. 
 
Historial de conversación:
{historial}
 
Responde de manera clara y concisa a la siguiente pregunta: {mensaje}"""
)
    
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

    