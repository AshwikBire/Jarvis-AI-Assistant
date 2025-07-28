import streamlit as st
from modules.chat import gemini_chat
from modules.voice import listen_command, speak_response
from modules.pdf_reader import read_pdf_text
from modules.search_web import search_duckduckgo
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("AIzaSyC48094RjAvbcPdUfLdltouGvP7LB6cHwk")

st.set_page_config(page_title="Jarvis AI Assistant", page_icon="🤖", layout="wide")
st.title("🤖 Jarvis AI Assistant")

st.markdown("""
<style>
.css-1d391kg {background-color: #0e1117;}
h1, h2, h3, h4, h5, h6, p, label, div {color: #f5f5f5 !important;}
</style>
""", unsafe_allow_html=True)

st.sidebar.header("Jarvis Menu")
menu = st.sidebar.radio("Choose Tool", ["Chat", "Voice Command", "PDF Reader", "Web Search", "About"])

if menu == "Chat":
    user_input = st.text_area("You:", placeholder="Ask anything...", height=100)
    if st.button("Send"):
        with st.spinner("Jarvis is thinking..."):
            reply = gemini_chat(user_input, GEMINI_API_KEY)
            st.markdown(f"**Jarvis:** {reply}")

elif menu == "Voice Command":
    st.info("Click below to speak")
    if st.button("🎤 Speak"):
        command = listen_command()
        st.write(f"You said: {command}")
        response = gemini_chat(command, GEMINI_API_KEY)
        st.markdown(f"**Jarvis:** {response}")
        speak_response(response)

elif menu == "PDF Reader":
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded_file:
        with st.spinner("Reading file..."):
            pdf_text = read_pdf_text(uploaded_file)
            st.text_area("PDF Content:", pdf_text, height=300)

elif menu == "Web Search":
    query = st.text_input("Enter search query")
    if st.button("Search"):
        results = search_duckduckgo(query)
        for r in results:
            st.markdown(f"- [{r['title']}]({r['href']})")

elif menu == "About":
    st.markdown("""
    ### Jarvis AI Assistant
    Built with ❤️ using Streamlit and Google Gemini API.
    - Chat with Google Gemini
    - Voice command and response
    - PDF Reader
    - Web Search
    """)
