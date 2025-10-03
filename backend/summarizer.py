
from transformers import pipeline

# Load the summarization model only once at startup
summarizer_pipeline = pipeline("summarization", model="t5-small")

def generate_summary(text, max_length=130, min_length=30):
    """
    Generate a summary for the given text using Hugging Face transformers.

    Args:
        text (str): Input text to summarize.
        max_length (int): Maximum tokens in the summary.
        min_length (int): Minimum tokens in the summary.

    Returns:
        str: Generated summary.
    """
    if not text.strip():
        return "No content provided to summarize."

    try:
        result = summarizer_pipeline(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )
        return result[0]['summary_text']
    except Exception as e:
        return f"Error generating summary: {str(e)}"