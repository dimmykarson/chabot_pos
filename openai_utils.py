import streamlit as st
import openai
from openai import AssistantEventHandler
import os, re
from typing_extensions import override
from dotenv import load_dotenv, find_dotenv



class OpenClient:
    def __init__(self):

        print("Carregando variáveis de ambiente")
        load_dotenv(find_dotenv())
        self.openai_key = st.secrets["OPENAI_API_KEY"]
        self.model = st.secrets["OPENAI_MODEL"]
        self.assistant_id = st.secrets["OPENAI_ASSISTANT_ID"]
        self.vector_store_id = st.secrets["OPENAI_VECTOR_STORE_ID"]


        self.client = openai.Client(api_key=self.openai_key)

        self.assistant = self.client.beta.assistants.retrieve(self.assistant_id)
        self.vector_store = self.client.vector_stores.retrieve(self.vector_store_id)

    
    def create_thread(self):
        print(":: Criando nova thread!")
        thread = self.client.beta.threads.create()
        return thread
    
    def get_answer(self, 
                   prompt, 
                   chat=None, 
                   thread=None):
        if not thread:
            thread = self.create_thread()

        self.client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=prompt
        )

        event_handler = EventHandler(chat)

        with self.client.beta.threads.runs.stream(
            thread_id=thread.id,
            assistant_id=self.assistant.id,
            event_handler=event_handler,
            tools=[{"type":"file_search"}],
            ) as stream:
                stream.until_done()


        event_handler.full_response = remove_brackets(event_handler.full_response)
        event_handler.placeholder.markdown(event_handler.full_response)
        return event_handler.full_response, thread


class EventHandler(AssistantEventHandler):
    
  def __init__(self, chat):
      super().__init__()
      self.full_response = ""
      self.chat = chat
      self.placeholder = chat.empty()
      self.placeholder.markdown("▌")
        
  @override
  def on_text_created(self, text) -> None:
    pass
      
  @override
  def on_text_delta(self, delta, snapshot):
      self.full_response += delta.value
      self.placeholder.markdown(self.full_response + " │")
      
  def on_tool_call_created(self, tool_call):
    pass
  
  def on_tool_call_delta(self, delta, snapshot):
    if delta.type == 'code_interpreter':
        if delta.code_interpreter.input:
            self.full_response += delta.code_interpreter.input
        if delta.code_interpreter.outputs:
            self.full_response += "\n\n"
            for output in delta.code_interpreter.outputs:
                if output.type == "logs":
                    self.full_response += f"\n{output.logs}"


def remove_brackets(text):
    # Expressão regular para encontrar tudo entre 【 e 】
    pattern = r'【.*?】'
    # Substitui qualquer correspondência pela string vazia
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text.strip().replace('【', '').replace('】', '')