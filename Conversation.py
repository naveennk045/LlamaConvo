import streamlit as st
import sys
import os,time
from groq import InternalServerError
from Llama import prompt

# Streamlit app setup
st.title("💬 LlamaConvo")
st.caption("🚀 A Streamlit chatbot powered by the Meta Llama")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I assist you today?"}]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
if prompt_text := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt_text})
    st.chat_message("user").write(prompt_text)
    try:
    # Get response from Llama model
        response = prompt(prompt_text)
    except InternalServerError:
        e="Try Again"
        st.exception(e)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)

        

