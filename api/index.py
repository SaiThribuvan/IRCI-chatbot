from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)

# Allow frontend (same project) to call backend
CORS(app, resources={r"/*": {"origins": "*"}})

# Load API key (set in Vercel)
api_key = os.getenv("AI_SECRET")
if not api_key:
    raise ValueError("API key not found. Set it in Vercel environment variables.")

genai.configure(api_key=api_key)

@app.route("/", methods=['GET'])
def home():
    return jsonify({"message": "Flask chatbot is running!"}), 200

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message')

        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        response_text = f"AI Response to: {user_message}"  # Replace with actual AI response
        return jsonify({'response': response_text}), 200

    except Exception as e:
        return jsonify({'error': f"Internal Server Error: {str(e)}"}), 500

# Required for Vercel
def handler(event, context):
    return app(event, context)
