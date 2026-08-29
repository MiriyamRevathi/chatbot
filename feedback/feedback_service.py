"""
Feedback Collection & Analytics Service.
"""

from repositories.feedback_repository import feedback_repository
from feedback.satisfaction_scorer import satisfaction_scorer

class FeedbackService:
    """Service managing user ratings and satisfaction scores."""

    def submit_feedback(self, message_id: str, conversation_id: str, is_helpful: bool, comment: str = "") -> dict:
        """Submit feedback rating."""
        return feedback_repository.add_feedback(message_id, conversation_id, is_helpful, comment)

    def get_satisfaction_metrics() -> dict:
        """Get current satisfaction score summary."""
        return satisfaction_scorer.calculate_score()

feedback_service = FeedbackService()
