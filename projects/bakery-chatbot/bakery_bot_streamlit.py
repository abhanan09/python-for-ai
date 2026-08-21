#bakery bot

import os

import streamlit as st
from google import genai
from google.genai import types

api_key = os.environ.get("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

st.set_page_config(page_title="Sweet Treats Bakery" , page_icon="🧁")

st.title("🧁Sweet Treats Bakery")
st.caption("Ask me about our menu, hours, or place an order!")

if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=api_key)

if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.client.chats.create(
        model = "gemini-3.6-flash",
        config = types.GenerateContentConfig(
            system_instruction = "You are a friendly customer support assistant for 'Sweet Treats Bakery'. Only answer questions about the bakery's products, hours, and orders. Bakery hours are 9 AM to 7 PM, Monday to Saturday. You sell cakes, cupcakes, and pastries. If asked anything unrelated to the bakery, politely redirect the conversation back to bakery topics."
    ),
)

if "messages" not in st.session_state:
    st.session_state.messages = []    

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])    


user_input = st.chat_input("Ask about our bakery....")

if user_input:

    st.session_state.messages.append({"role": "user" ,"content" : user_input})

    try:
        with st.spinner("Thinking..."):
            response = st.session_state.chat.send_message(user_input)
        st.session_state.messages.append({"role" : "assistant" ,"content" : response.text})

    except Exception as e: #noqa
          st.session_state.messages.append({"role" : "assistant" ,"content" : "Sorry! I am having trouble responding right now. Please try again."})

    st.rerun()