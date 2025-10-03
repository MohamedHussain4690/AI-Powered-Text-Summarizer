import re
import nltk

# Ensure required nltk data is available
nltk.download("punkt", quiet=True)

def clean_text(text: str) -> str:
    """
    Basic text cleaning for summarization.
    Removes extra spaces, special characters, and normalizes text.
    """
    # Remove newlines and multiple spaces
    text = re.sub(r"\s+", " ", text)
    # Remove unwanted characters (keeping words, numbers, punctuation)
    text = re.sub(r"[^a-zA-Z0-9.,!?;:()\"'’ ]", "", text)
    return text.strip()

def tokenize_sentences(text: str) -> list[str]:
    """
    Tokenize text into sentences for preprocessing.
    """
    from nltk.tokenize import sent_tokenize
    return sent_tokenize(text)

def preprocess_input(text: str) -> str:
    """
    Full preprocessing pipeline:
    - Clean text
    - (Optionally) ensure minimum sentence length
    """
    cleaned = clean_text(text)
    sentences = tokenize_sentences(cleaned)
    # Keep only sentences with at least 3 words
    filtered = [s for s in sentences if len(s.split()) > 2]
    return " ".join(filtered)
