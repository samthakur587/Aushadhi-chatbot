import streamlit as st
from unify import Unify
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up Unify API
api_key = os.getenv('UNIFY_API_KEY')
endpoint = os.getenv('UNIFY_ENDPOINT')
unify = Unify(api_key=api_key, endpoint=endpoint)


st.markdown("""
    <div style="text-align: center;">
        <h1 style="color: #EEEEEE;">Aushdhi AI Chatbot</h1>
        <h2 style="color: #DDDDDD;">🤖 Your Intelligent Healthcare Assistant</h2>
    </div>
""", unsafe_allow_html=True)
#cont1 = st.container(height=500)
prompt = st.chat_input("Say something")

# Process the input and display the response
if prompt:
    message1 =  st.chat_message("user")
    message1.write(prompt)
    try:
        response = unify.generate(prompt)
        message2 = st.chat_message("AI")
        message2.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
