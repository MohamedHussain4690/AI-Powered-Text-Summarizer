from flask import Flask, request, jsonify
from summarizer import generate_summary
from preprocess import clean_text

app = Flask(__name__)

@app.route("/summarize", methods=["POST"])
def summarize():
    """
    API endpoint: accepts JSON with text, returns summarized text.
    """
    data = request.get_json()
    text = data.get("text", "")

    if not text.strip():
        return jsonify({"error": "No text provided"}), 400

    # Preprocess before summarizing
    cleaned_text = clean_text(text)

    try:
        summary = generate_summary(cleaned_text)
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def home():
    """
    Simple health check endpoint.
    """
    return jsonify({"message": "AI Summarizer Backend is running"})


if __name__ == "__main__":
    app.run(debug=True)
