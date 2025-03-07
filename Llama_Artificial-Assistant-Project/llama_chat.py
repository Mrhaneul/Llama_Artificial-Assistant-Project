from langchain_ollama import OllamaLLM
from ollama import chat, ChatResponse
from open_app import open_application

while True:
    user_input = input("Enter your question: ")  # Always shows this prompt first

    if user_input.lower() == "bye":
        print("Goodbye!")
        break
    
    if user_input.lower() == "open":  # Only opens an app if user types "open"
        app_name = input("Enter the name of the application to open: ")
        open_application(app_name)
        continue  # Restart the loop without calling the chat model

    # Call the AI chat only if the user is not opening an app
    messages = [
        {'role': 'user', 'content': user_input},
    ]

    for part in chat('llama3.2', messages=messages, stream=True):
        print(part['message']['content'], end='', flush=True)

    print()  # Print a newline after the response