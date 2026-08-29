"""
N-Gram Extraction Engine.
"""

from nlp.tokenizer import Tokenizer

class NGramExtractor:
    """Extract Unigrams, Bigrams, and Trigrams."""

    @staticmethod
    def extract_ngrams(tokens: list, n: int = 2) -> list:
        """Generate contiguous sequence of n tokens."""
        if len(tokens) < n:
            return []
        return [" ".join(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]

    @classmethod
    def get_all_ngrams(cls, text: str, max_n: int = 3) -> dict:
        """Extract all n-grams up to max_n from raw text."""
        tokens = Tokenizer.tokenize_words(text)
        result = {}
        for i in range(1, max_n + 1):
            result[f"{i}-grams"] = cls.extract_ngrams(tokens, i)
        return result

ngram_extractor = NGramExtractor()
