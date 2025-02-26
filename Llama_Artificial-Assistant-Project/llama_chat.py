from langchain_ollama import OllamaLLM
from ollama import chat, ChatResponse

while True:
    user_input = input("Enter your question: ")  # Always shows this prompt first

    if user_input.lower() == "bye":
        print("Goodbye!")
        break
    
    from open_app import open_application
    
    if user_input.lower() == "open":  # Only opens an app if user types "open"
        app_name = input("Enter the name of the application to open: ")
        open_application(app_name)
        continue  # Restart the loop without calling the chat model

    # Call the AI chat only if the user is not opening an app
    response: ChatResponse = chat(model='llama3.2', messages=[
        {'role': 'user', 'content': user_input},
    ])

    print(response.message.content)
