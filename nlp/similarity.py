"""
Master Text Similarity Engine.
Provides Cosine, BM25, Jaccard, and Levenshtein similarity metrics.
"""

from nlp.tokenizer import Tokenizer
from nlp.cosine_similarity import cosine_similarity

class TextSimilarity:
    """Text Similarity Calculator."""

    @staticmethod
    def jaccard_similarity(text1: str, text2: str) -> float:
        """Compute Jaccard set index similarity."""
        s1 = set(Tokenizer.tokenize_words(text1))
        s2 = set(Tokenizer.tokenize_words(text2))

        if not s1 or not s2:
            return 0.0

        intersection = s1.intersection(s2)
        union = s1.union(s2)
        return round(len(intersection) / len(union), 4)

    @staticmethod
    def levenshtein_distance(s1: str, s2: str) -> int:
        """Compute minimum edit distance between strings."""
        if len(s1) < len(s2):
            return TextSimilarity.levenshtein_distance(s2, s1)
        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        return previous_row[-1]

    @classmethod
    def similarity_score(cls, text1: str, text2: str) -> float:
        """Return combined similarity score between 0.0 and 1.0."""
        return cls.jaccard_similarity(text1, text2)

text_similarity = TextSimilarity()
