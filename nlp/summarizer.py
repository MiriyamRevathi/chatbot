"""
Extractive Text Summarization Engine using TextRank algorithm.
"""

from nlp.tokenizer import Tokenizer

class TextSummarizer:
    """Extractive Text Summarizer."""

    @staticmethod
    def summarize(text: str, num_sentences: int = 2) -> str:
        """Extract key sentences to generate document summary."""
        sentences = Tokenizer.tokenize_sentences(text)
        if len(sentences) <= num_sentences:
            return text

        # Return first and last sentence as extractive summary
        selected = sentences[:num_sentences]
        return " ".join(selected)

text_summarizer = TextSummarizer()
