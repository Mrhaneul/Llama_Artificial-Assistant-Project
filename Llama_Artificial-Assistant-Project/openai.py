import openai

openai.base_url = "http://localhost:11434/v1"
openai.api_key = 'ollama'

user_input = input("Input: ")  # Always shows this prompt first

messages = [
        {'role': 'user', 'content': user_input},
    ]
tools = []

response = openai.chat.completions.create(
	model="llama3.2",
	messages=messages,
	tools=tools,
)

print(response)