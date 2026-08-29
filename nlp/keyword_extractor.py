"""
RAKE and TF-IDF Keyword Extraction Algorithms.
"""

from collections import Counter
from nlp.tokenizer import Tokenizer
from nlp.stopwords import remove_stopwords

class KeywordExtractor:
    """Keyword Extractor."""

    @staticmethod
    def extract_keywords(text: str, top_n: int = 5) -> list:
        """Extract top N keywords using word frequency after stopword removal."""
        tokens = Tokenizer.tokenize_words(text)
        filtered = remove_stopwords(tokens)
        counts = Counter(filtered)
        return [w for w, c in counts.most_common(top_n)]

keyword_extractor = KeywordExtractor()
