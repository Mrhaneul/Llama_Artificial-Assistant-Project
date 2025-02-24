import requests
import json

if __name__ == '__server__':
    num_questions = 3
    question_num = 0

    while question_num < num_questions:
        question = str(input("Enter your question: "))
        data = {
            "model": "llama3.2",
            "messages": [
                {
                    "role": "user",
                        "content": question,
                        "stream": False
                    }
                ]
            }
        url = "http://localhost:11434/api/chat"
        response = requests.post(url, json=data)
        question_num += 1

    response_json = json.loads(response.text)
    ai_reply = response_json['message']['content']
    print(ai_reply)
        