import logging
from datetime import datetime
logging.basicConfig(
    filename="summarizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_request(input_text: str, summary: str) -> None:
    """
    Log user input and generated summary.
    """
    logging.info("INPUT: %s", input_text[:200])  
    logging.info("SUMMARY: %s", summary)

def format_response(summary: str, metadata: dict = None) -> dict:
    """
    Format API response with optional metadata.
    """
    response = {"summary": summary}
    if metadata:
        response["metadata"] = metadata
    return response

def timestamp() -> str:
    """
    Return current timestamp string.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
