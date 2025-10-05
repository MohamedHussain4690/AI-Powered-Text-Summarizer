from transformers import pipeline
summarizer_pipeline = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)
def chunk_text(text: str, max_words: int = 400):
    """
    Split long text into smaller chunks for summarization.
    """
    words = text.split()
    for i in range(0, len(words), max_words):
        yield " ".join(words[i:i + max_words])

def generate_summary(text: str) -> str:
    """
    Generate a high-quality summary from long or multi-paragraph text.
    Handles chunking, summarizing each part, and merging final results.
    """
    if not text.strip():
        return "No content provided to summarize."

    try:
        text = text.strip().replace("\n", " ")
        chunks = list(chunk_text(text))
        partial_summaries = []

        for chunk in chunks:
            num_words = len(chunk.split())
            max_length = min(500, int(num_words * 0.6))
            min_length = max(70, int(num_words * 0.25))

            result = summarizer_pipeline(
                chunk,
                max_length=max_length,
                min_length=min_length,
                do_sample=False,
                truncation=True
            )
            partial_summaries.append(result[0]['summary_text'].strip())
        combined_summary = " ".join(partial_summaries)
        if len(combined_summary.split()) > 300:
            final = summarizer_pipeline(
                combined_summary,
                max_length=250,
                min_length=80,
                do_sample=False,
                truncation=True
            )
            combined_summary = final[0]['summary_text'].strip()
        if not combined_summary.endswith(('.', '!', '?')):
            combined_summary += '.'

        return combined_summary

    except Exception as e:
        return f"Error generating summary: {str(e)}"
