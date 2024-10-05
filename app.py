import streamlit as st
import google.generativeai as ai
import re
import json

# Load sensitive data from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# API Key
API_KEY = config['api_key']

# Configure the API
ai.configure(api_key=API_KEY)

# Create a new model
model = ai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat()

# Initialize conversation history
if 'history' not in st.session_state:
    st.session_state.history = []

# Streamlit UI Layout
st.title("Chat with Pegasus")

# Display the chat history
if st.session_state.history:
    for message in st.session_state.history:
        if message.startswith("You:"):
            st.markdown(f"**{message}**")  # Display user prompt in bold
        else:
            st.markdown(f"Pegasus: {message}")  # Display Pegasus' response

# User input
user_input = st.text_input("Enter your prompt:", key="input")

# Handle the submission
if st.button("Submit") and user_input:
    # Add user message to conversation history
    st.session_state.history.append(f"You: {user_input}")
    
    # Send the full conversation history to the model
    response = chat.send_message('\n'.join(st.session_state.history))
    
    # Clean response text (remove ** or any unwanted formatting)
    cleaned_response = re.sub(r'\*\*', '', response.text)
    
    # Add AI response to conversation history
    st.session_state.history.append(f"{cleaned_response}")
    
    # Clear the input box for the next message
    st.session_state.input = ""
