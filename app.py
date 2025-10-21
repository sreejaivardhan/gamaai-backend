from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/healthz")
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route("/")
def home():
    return "🤖 GamaAI backend is running!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "No question provided"}), 400
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        answer = response.choices[0].message.content
        return jsonify({"reply": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
