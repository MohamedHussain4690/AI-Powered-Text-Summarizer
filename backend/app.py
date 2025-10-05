from flask import Flask, request, jsonify
from summarizer import generate_summary
from preprocess import preprocess_input
from flask_cors import CORS
app = Flask(__name__)

CORS(app) 

@app.route("/")
def home():
    return jsonify({"message": "AI Summarizer API is running!"})

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        data = request.get_json()
        text = data.get("text", "")
        print("📥 Received text:", text[:200]) 
        cleaned = preprocess_input(text)
        print("🧹 Cleaned text:", cleaned[:200])  

        summary = generate_summary(cleaned)
        print("🧠 Generated summary:", summary)  

        return jsonify({"summary": summary})

    except Exception as e:
        import traceback
        print("⚠️ ERROR in summarize():", e)
        traceback.print_exc() 
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
