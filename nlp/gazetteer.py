"""
Dictionary-based Named Entity Recognition (Gazetteer).
"""

GAZETTEER_ENTITIES = {
    "PRODUCT": ["ChatFlow", "NLP Lab", "Model Playground", "Pro Plan", "Enterprise Tier", "Vector Search"],
    "CATEGORY": ["Billing", "Account", "Technical", "Products", "Orders", "Security", "Subscriptions"],
    "SYS_COMPONENT": ["Flask", "scikit-learn", "TF-IDF", "Naive Bayes", "SQLite", "Docker", "Joblib"]
}

class GazetteerEntityExtractor:
    """Dictionary / Gazetteer Entity Extractor."""

    @staticmethod
    def extract(text: str) -> list:
        """Extract gazetteer entities."""
        entities = []
        text_lower = text.lower()
        for cat, items in GAZETTEER_ENTITIES.items():
            for item in items:
                if item.lower() in text_lower:
                    entities.append({
                        "entity": item,
                        "type": cat,
                        "confidence": 0.95
                    })
        return entities

gazetteer_extractor = GazetteerEntityExtractor()
