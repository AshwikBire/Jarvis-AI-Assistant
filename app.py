import streamlit as st
from chat import gemini_chat
from voice import listen_command, speak_response
from pdf_reader import read_pdf_text
from search_web import search_duckduckgo

import time
import requests
import json

import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("AIzaSyC48094RjAvbcPdUfLdltouGvP7LB6cHwk")

st.set_page_config(page_title="Jarvis AI", layout="wide", page_icon="🤖")

st.markdown("""
    <style>
    html, body, [class*="css"]  {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: 'Segoe UI', sans-serif;
    }
    .title-text {
        text-align: center;
        color: #58a6ff;
        font-size: 3em;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .section {
        background-color: #161b22;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    .chat-box {
        background-color: #21262d;
        padding: 0.8rem;
        border-radius: 10px;
        margin-bottom: 0.8rem;
    }
    .chat-user {color: #f0f6fc; font-weight: bold;}
    .chat-bot {color: #8b949e; margin-left: 1rem;}
    .stButton>button {
        background: linear-gradient(90deg, #1f6feb, #238636);
        color: white;
        border: none;
        padding: 0.6rem 1.2rem;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""<div class='title-text'>🤖 JARVIS - Your AI Assistant</div>""", unsafe_allow_html=True)

# Chat Section
with st.container():
    st.markdown("""<div class='section'>""", unsafe_allow_html=True)
    st.subheader("💬 Talk to Jarvis")
    user_input = st.text_area("Your Question:", placeholder="Type here...", height=100)
    if st.button("Ask Jarvis"):
        if user_input:
            with st.spinner("Jarvis is processing..."):
                start = time.time()
                reply = gemini_chat(user_input, AIzaSyC48094RjAvbcPdUfLdltouGvP7LB6cHwk)
                end = time.time()
                st.session_state.chat_history = st.session_state.get("chat_history", [])
                st.session_state.chat_history.append((user_input, reply))
                st.success(f"Jarvis replied in {end - start:.2f} seconds")

    if "chat_history" in st.session_state:
        for u, r in reversed(st.session_state.chat_history[-5:]):
            st.markdown(f"""
                <div class='chat-box'>
                    <div class='chat-user'>🧑 You:</div>
                    <div>{u}</div>
                    <div class='chat-bot'>🤖 Jarvis:</div>
                    <div>{r}</div>
                </div>
            """, unsafe_allow_html=True)
    st.markdown("""</div>""", unsafe_allow_html=True)

# Voice Assistant Section
with st.container():
    st.markdown("""<div class='section'>""", unsafe_allow_html=True)
    st.subheader("🎤 Voice Assistant")
    if st.button("🎙️ Start Listening"):
        command = listen_command()
        st.write(f"🗣️ Detected: `{command}`")
        with st.spinner("Jarvis is thinking..."):
            response = gemini_chat(command, GEMINI_API_KEY)
            st.markdown(f"**🤖 Jarvis:** {response}")
            speak_response(response)
    st.markdown("""</div>""", unsafe_allow_html=True)

# PDF Reader Section
with st.container():
    st.markdown("""<div class='section'>""", unsafe_allow_html=True)
    st.subheader("📘 Read PDF File")
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")
    if uploaded_file:
        with st.spinner("Reading PDF..."):
            pdf_text = read_pdf_text(uploaded_file)
            st.text_area("PDF Content:", pdf_text, height=300)
    st.markdown("""</div>""", unsafe_allow_html=True)

# Web Search Section
with st.container():
    st.markdown("""<div class='section'>""", unsafe_allow_html=True)
    st.subheader("🌐 DuckDuckGo Web Search")
    query = st.text_input("Enter your query:")
    if st.button("Search Web"):
        with st.spinner("Searching the web..."):
            results = search_duckduckgo(query)
            for r in results:
                st.markdown(f"- [{r['title']}]({r['href']})")
    st.markdown("""</div>""", unsafe_allow_html=True)

# Footer
st.markdown("""<p style='text-align: center; color: gray;'>🚀 Powered by Google Gemini API | Made by Ashwik Bire</p>""", unsafe_allow_html=True)

 