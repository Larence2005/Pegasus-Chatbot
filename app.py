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
history = []

# Start a conversation
print('Hi! My name is Pegasus, how can I help you?')
while True:
    message = input('\nYou: ')
    if message.lower() == 'bye':
        print('Pegasus: Goodbye!')
        break

    # Add user message to conversation history
    history.append(f"You: {message}")

    # Send the full conversation history to the model
    response = chat.send_message('\n'.join(history))

    # Clean response text (remove ** or any unwanted formatting)
    cleaned_response = re.sub(r'\*\*', '', response.text)

    # Add AI response to conversation history
    history.append(f"Pegasus: {cleaned_response}")

    print(f'Pegasus: {cleaned_response}')
