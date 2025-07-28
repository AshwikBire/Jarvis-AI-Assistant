import streamlit as st
from chat import gemini_chat
from voice import listen_command, speak_response
from pdf_reader import read_pdf_text
from search_web import search_duckduckgo

import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("AIzaSyC48094RjAvbcPdUfLdltouGvP7LB6cHwk")

st.set_page_config(page_title="Jarvis AI Assistant", page_icon="🤖", layout="wide")

st.markdown("""
    <style>
    .main {background-color: #0F1117; color: white;}
    .block-container {padding: 2rem 2rem;}
    .stButton>button {background-color: #4CAF50; color: white; padding: 10px 24px; border: none; border-radius: 12px;}
    .stTextInput>div>div>input {background-color: #1E1E1E; color: white;}
    .stTextArea>div>textarea {background-color: #1E1E1E; color: white;}
    .stMarkdown {font-size: 1.1rem;}
    </style>
""", unsafe_allow_html=True)

st.markdown("""<h1 style='text-align: center; color: cyan;'>🤖 Welcome to Jarvis AI Assistant</h1>""", unsafe_allow_html=True)

st.sidebar.markdown("## 🚀 Jarvis Menu")
menu = st.sidebar.radio("Select Feature", ["🧠 Chat with Jarvis", "🎙️ Voice Assistant", "📄 PDF Reader", "🌐 Web Search", "ℹ️ About"], index=0)

if menu == "🧠 Chat with Jarvis":
    st.markdown("### 💬 Chat Mode")
    user_input = st.text_area("Type your question below:", placeholder="Ask me anything...", height=100)
    if st.button("🔍 Get Response"):
        with st.spinner("🤖 Jarvis is thinking..."):
            reply = gemini_chat(user_input, GEMINI_API_KEY)
            st.markdown(f"**🧠 Jarvis:** {reply}")

elif menu == "🎙️ Voice Assistant":
    st.markdown("### 🎤 Speak to Jarvis")
    st.info("Click the button below and speak your question")
    if st.button("🎙️ Start Listening"):
        command = listen_command()
        st.write(f"🗣️ You said: `{command}`")
        with st.spinner("🎧 Processing your voice..."):
            response = gemini_chat(command, GEMINI_API_KEY)
            st.markdown(f"**🧠 Jarvis:** {response}")
            speak_response(response)

elif menu == "📄 PDF Reader":
    st.markdown("### 📘 Upload and Read a PDF")
    uploaded_file = st.file_uploader("Choose your PDF file", type="pdf")
    if uploaded_file:
        with st.spinner("📄 Extracting text from PDF..."):
            pdf_text = read_pdf_text(uploaded_file)
            st.text_area("📄 PDF Content:", pdf_text, height=300)

elif menu == "🌐 Web Search":
    st.markdown("### 🔍 Web Search Tool")
    query = st.text_input("Enter your query below:", placeholder="Search anything on the web")
    if st.button("🌐 Search"):
        with st.spinner("Searching the web..."):
            results = search_duckduckgo(query)
            for r in results:
                st.markdown(f"- [{r['title']}]({r['href']})")

elif menu == "ℹ️ About":
    st.markdown("""
        ## ℹ️ About Jarvis
        **Jarvis AI** is your personal AI assistant powered by **Google Gemini API**.

        **Features include:**
        - 🧠 Natural Language Chat
        - 🎙️ Voice Command Interface
        - 📄 Intelligent Document Reading
        - 🌐 Real-Time Web Search

        **Technologies Used:** Streamlit, Gemini API, TTS, Voice Recognition, DuckDuckGo

        _Created with ❤️ by Ashwik Bire_
    """)
