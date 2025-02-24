import ollama

response = ollama.chat(
    model='llama3.2',
    messages=[{'role': 'user', 'content':
        'Open Chrome'}],

		# Opens the indicated app
    tools=[{
      'type': 'function',
      'function': {
        'name': 'find_and_open_app',
        'description': 'Open the indicated app',
        'parameters': {
          'type': 'object',
          'properties': {
            'app': {
              'type': 'string',
              'description': 'The name of the app',
            },
          },
          'required': ['app'],
        },
      },
    },
  ],
)

print(response['message']['tool_calls'])