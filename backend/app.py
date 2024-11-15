# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing


# backend/app.py

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('input', '')
    
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'user', 'content': user_input}
            ]
        )
        message = response['choices'][0]['message']['content']
        return jsonify({'message': message})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'An error occurred while communicating with OpenAI API.'}), 500

if __name__ == '__main__':
    app.run(port=5000)