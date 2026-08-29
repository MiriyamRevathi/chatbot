"""
Tokenization Engine.
"""

import re

class Tokenizer:
    """Word and Sentence Tokenizer."""

    @staticmethod
    def tokenize_words(text: str) -> list:
        """Tokenize text into lowercased words using regex."""
        if not text:
            return []
        pattern = r"\b\w+\b"
        return re.findall(pattern, text.lower())

    @staticmethod
    def tokenize_sentences(text: str) -> list:
        """Split text into sentences using punctuation boundaries."""
        if not text:
            return []
        pattern = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s"
        sentences = re.split(pattern, text)
        return [s.strip() for s in sentences if s.strip()]

tokenizer = Tokenizer()
