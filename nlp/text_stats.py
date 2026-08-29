"""
Text Statistics and Readability Scoring Engine.
"""

import math
import re
from nlp.tokenizer import Tokenizer

class TextStats:
    """Analyzer for Text Readability & Lexical Complexity."""

    @staticmethod
    def analyze(text: str) -> dict:
        """Compute character, word, sentence, and readability stats."""
        if not text:
            return {
                "char_count": 0, "word_count": 0, "sentence_count": 0,
                "lexical_diversity": 0.0, "flesch_reading_ease": 0.0, "gunning_fog": 0.0
            }

        chars = len(text)
        words = Tokenizer.tokenize_words(text)
        word_count = len(words)
        sentences = Tokenizer.tokenize_sentences(text)
        sentence_count = max(1, len(sentences))

        unique_words = set(words)
        lexical_diversity = round(len(unique_words) / word_count, 4) if word_count > 0 else 0.0

        # Syllable approximation
        def count_syllables(w):
            w = w.lower()
            if len(w) <= 3: return 1
            w = re.sub(r'(?:[^laeiouy]es|ed|e)$', '', w)
            w = re.sub(r'^y', '', w)
            syllables = len(re.findall(r'[aeiouy]{1,2}', w))
            return max(1, syllables)

        total_syllables = sum(count_syllables(w) for w in words)
        complex_words = sum(1 for w in words if count_syllables(w) >= 3)

        # Flesch Reading Ease Formula
        if word_count > 0 and sentence_count > 0:
            fre = 206.835 - (1.015 * (word_count / sentence_count)) - (84.6 * (total_syllables / word_count))
            fog = 0.4 * ((word_count / sentence_count) + 100.0 * (complex_words / word_count))
        else:
            fre = 0.0
            fog = 0.0

        return {
            "char_count": chars,
            "word_count": word_count,
            "sentence_count": sentence_count,
            "lexical_diversity": lexical_diversity,
            "flesch_reading_ease": round(fre, 2),
            "gunning_fog": round(fog, 2)
        }

text_stats = TextStats()
