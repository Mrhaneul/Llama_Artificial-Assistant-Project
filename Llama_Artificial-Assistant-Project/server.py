from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/chat/', methods=['POST'])
def chat():
    data = request.get_json()
    question = data['messages'][0]['content']
    # Process the question and generate a response
    ai_reply = f"Received your question: {question}"
    response = {
        "message": {
            "content": ai_reply
        }
    }
    return jsonify(response)

if __name__ == '__server__':
    app.run(host='0.0.0.0', port=5000)