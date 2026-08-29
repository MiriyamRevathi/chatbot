"""
Text Preprocessing Module.
"""

import re
import string
from nlp.stopwords import remove_stopwords

class TextPreprocessor:
    """Text Preprocessor for NLP Pipeline."""

    def __init__(self, lower=True, remove_punct=True, remove_digits=False, strip_html=True):
        self.lower = lower
        self.remove_punct = remove_punct
        self.remove_digits = remove_digits
        self.strip_html = strip_html

    def clean(self, text: str) -> str:
        """Apply comprehensive cleaning pipeline to raw text."""
        if not text or not isinstance(text, str):
            return ""

        cleaned = text.strip()

        if self.strip_html:
            cleaned = re.sub(r"<[^>]+>", " ", cleaned)

        # Normalize whitespace
        cleaned = re.sub(r"\s+", " ", cleaned)

        if self.lower:
            cleaned = cleaned.lower()

        if self.remove_digits:
            cleaned = re.sub(r"\d+", "", cleaned)

        if self.remove_punct:
            translator = str.maketrans("", "", string.punctuation)
            cleaned = cleaned.translate(translator)

        return cleaned.strip()

preprocessor = TextPreprocessor()
