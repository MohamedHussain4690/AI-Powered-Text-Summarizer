from flask import Flask, request, jsonify
from summarizer import generate_summary
from preprocess import preprocess_input
from utils import log_request, format_response, timestamp
from flask_cors import CORS
app = Flask(__name__)

CORS(app)  # <--- enables CORS for all routes

@app.route("/")
def home():
    return jsonify({"message": "AI Summarizer API is running!"})

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        data = request.get_json()
        text = data.get("text", "")
        print("📥 Received text:", text[:200])  # debug input
        cleaned = preprocess_input(text)
        print("🧹 Cleaned text:", cleaned[:200])  # debug output

        summary = generate_summary(cleaned)
        print("🧠 Generated summary:", summary)  # debug summary

        return jsonify({"summary": summary})

    except Exception as e:
        import traceback
        print("⚠️ ERROR in summarize():", e)
        traceback.print_exc()  # <-- will now print full error
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
