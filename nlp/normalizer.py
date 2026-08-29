"""
Text Normalization Engine.
"""

import re
import unicodedata

CONTRACTIONS = {
    "can't": "cannot", "won't": "will not", "n't": " not",
    "'re": " are", "'s": " is", "'d": " would", "'ll": " will",
    "'t": " not", "'ve": " have", "'m": " am"
}

class TextNormalizer:
    """Comprehensive Text Normalizer."""

    @staticmethod
    def expand_contractions(text: str) -> str:
        """Expand English contractions."""
        for c, expanded in CONTRACTIONS.items():
            text = re.sub(c, expanded, text, flags=re.IGNORECASE)
        return text

    @staticmethod
    def normalize_unicode(text: str) -> str:
        """Convert unicode characters to ASCII representation."""
        return unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("utf-8")

    @classmethod
    def normalize(cls, text: str) -> str:
        """Apply full normalization suite."""
        if not text:
            return ""
        expanded = cls.expand_contractions(text)
        cleaned = cls.normalize_unicode(expanded)
        return cleaned.strip()

normalizer = TextNormalizer()
