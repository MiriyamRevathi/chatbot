"""
Multi-Factor Confidence Scoring Calculator.
Combines Intent probability, Sentiment alignment, Entity presence, and Knowledge base score.
"""

class ConfidenceScorer:
    """Confidence Scoring Engine."""

    @staticmethod
    def calculate(intent_prob: float, sentiment_conf: float, has_entities: bool, kb_score: float = 0.0) -> float:
        """Compute composite confidence score between 0.0 and 1.0."""
        weight_intent = 0.50
        weight_kb = 0.30
        weight_sentiment = 0.10
        weight_entities = 0.10

        entity_score = 1.0 if has_entities else 0.5

        composite = (
            (intent_prob * weight_intent) +
            (kb_score * weight_kb) +
            (sentiment_conf * weight_sentiment) +
            (entity_score * weight_entities)
        )

        return round(min(1.0, max(0.0, composite)), 4)

confidence_scorer = ConfidenceScorer()
