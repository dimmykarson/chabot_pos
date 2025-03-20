import streamlit as st
import os
import time
from PIL import Image
from openai_utils import OpenClient


im = Image.open("imgs/bird_2.jpg")
logo = Image.open("imgs/bird_2.jpg")

st.set_page_config(page_title="Chat Bot Pós iCEV", 
                   page_icon=im, 
                   layout="wide")

def main():
    col1, col2 = st.columns([.1, .9])
    col1.image(logo, width=180)

    if not "client" in st.session_state:
        st.session_state.client = OpenClient()

    client = st.session_state.client

    if not 'messages' in st.session_state:
        st.session_state.messages = []

    if not 'thread' in st.session_state:
        st.session_state.thread = client.create_thread()

    messages = st.session_state['messages']

    if len(messages) == 0:
        messages = [
            {
                "role": "assistant",
                "content": "Olá! Sou Rebeca, o Chatbot da Pós iCEV. Qual é seu nome e como posso te ajudar?"
            }
        ]

    for msg in messages:
        chat = st.chat_message(msg['role'])
        chat.markdown(msg['content'])

    prompt = st.chat_input("Pergunte algo, meu caro!")
    if prompt:
        new_message = {
            "role": "user",
            "content": prompt
        }
        chat = st.chat_message(new_message['role'])
        chat.markdown(new_message['content'])
        messages.append(new_message)
        
        chat = st.chat_message('assistant')
        full_response, thread = client.get_answer(prompt, chat, st.session_state.thread)
        
        new_message = {'role': 'assistant',
                         'content': full_response}
        messages.append(new_message)
        st.session_state['messages'] = messages
        st.session_state['thread'] = thread


main()