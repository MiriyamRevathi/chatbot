"""
Pattern-based Named Entity Recognition Engine.
"""

import re

PATTERNS = {
    "EMAIL": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "PHONE": r"(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "ORDER_ID": r"ORD-\d{5,8}",
    "CURRENCY": r"\$\d+(?:\.\d{2})?",
    "ACCOUNT_NUM": r"ACC-\d{6,10}",
    "URL": r"https?://[^\s]+",
    "DATE": r"\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{4}"
}

class RegexEntityExtractor:
    """Regex Pattern Entity Extractor."""

    @staticmethod
    def extract(text: str) -> list:
        """Extract regex pattern entities from text."""
        entities = []
        for entity_type, pattern in PATTERNS.items():
            matches = re.finditer(pattern, text)
            for m in matches:
                entities.append({
                    "entity": m.group(0),
                    "type": entity_type,
                    "start": m.start(),
                    "end": m.end()
                })
        return entities

regex_entity_extractor = RegexEntityExtractor()

# Expanded Pattern Regex & Gazetteer NER Rules
