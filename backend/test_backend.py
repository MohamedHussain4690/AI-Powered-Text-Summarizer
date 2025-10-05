import requests
import json

API_URL = "http://127.0.0.1:5000/summarize"

def test_summary(text: str):
    """
    Send a test request to the summarizer API and print the response.
    """
    try:
        payload = {"text": text}
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        print(json.dumps(data, indent=2))
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    samples = [
        "Artificial intelligence is transforming industries by automating tasks, "
        "providing insights, and enabling new ways of working. From healthcare to "
        "finance, AI applications are driving efficiency and innovation.",

        "Machine learning enables computers to learn from data without being explicitly programmed, "
        "allowing systems to improve their performance over time."
    ]

    for idx, text in enumerate(samples, start=1):
        print(f"\n--- Test {idx} ---")
        test_summary(text)
