from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "🤖 GamaAI backend is running!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )

    answer = response["choices"][0]["message"]["content"]
    return jsonify({"reply": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
