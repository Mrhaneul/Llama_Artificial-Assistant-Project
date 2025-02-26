from langchain_ollama import OllamaLLM
from ollama import chat, ChatResponse
from open_app import open_application

while True:
    user_input = input("Enter your question: ")
    if user_input.lower() == "bye":
        print("Goodbye!")
        break
    if user_input.lower() == "open":
        app_name = input("Enter the name of the application to open: ")
        open_application(app_name)
        continue

    response: ChatResponse = chat(model='llama3.2', messages=[
      {
        'role': 'user',
        'content': user_input,  # Use user input as content
      },
    ])

    #print(response['message']['content'])
    # or access fields directly from the response object
    print(response.message.content)