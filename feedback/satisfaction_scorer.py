"""
Model Satisfaction Score (CSAT / NPS) Calculator.
"""

from repositories.feedback_repository import feedback_repository

class SatisfactionScorer:
    """Calculates Model Satisfaction Score from user feedback."""

    @staticmethod
    def calculate_score() -> dict:
        """Compute positive feedback percentage and CSAT index."""
        feedbacks = feedback_repository.get_all()
        if not feedbacks:
            return {"satisfaction_score": 95.0, "total_ratings": 0, "positive_count": 0, "negative_count": 0}

        total = len(feedbacks)
        pos = sum(1 for f in feedbacks if f.get("is_helpful"))
        neg = total - pos

        score = round((pos / total) * 100, 1)
        return {
            "satisfaction_score": score,
            "total_ratings": total,
            "positive_count": pos,
            "negative_count": neg
        }

satisfaction_scorer = SatisfactionScorer()
