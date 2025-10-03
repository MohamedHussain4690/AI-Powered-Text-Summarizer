from flask import Flask, request, jsonify
from summarizer import generate_summary
from preprocess import preprocess_input
from utils import log_request, format_response, timestamp

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "AI Summarizer API is running!"})

@app.route("/summarize", methods=["POST"])
def summarize():
    """
    API endpoint: accepts JSON { "text": "your long text" }
    Returns: JSON { "summary": "short text", "metadata": {...} }
    """
    try:
        data = request.get_json()
        if not data or "text" not in data:
            return jsonify({"error": "Missing 'text' field"}), 400

        raw_text = data["text"]
        cleaned_text = preprocess_input(raw_text)
        summary = generate_summary(cleaned_text)

        # log the request/response
        log_request(raw_text, summary)

        # return structured response
        return jsonify(format_response(summary, {"timestamp": timestamp()}))

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
