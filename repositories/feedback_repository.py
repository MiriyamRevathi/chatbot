"""
Feedback Repository for User Ratings and Comments.
"""

from repositories.base_repository import BaseRepository
from datetime import datetime
import uuid

class FeedbackRepository(BaseRepository):
    """Repository managing User Chatbot Ratings."""

    def __init__(self):
        super().__init__("feedback.json")

    def add_feedback(self, message_id: str, conversation_id: str, is_helpful: bool, comment: str = None) -> dict:
        """Record user feedback rating."""
        fb = {
            "id": str(uuid.uuid4()),
            "message_id": message_id,
            "conversation_id": conversation_id,
            "is_helpful": is_helpful,
            "comment": comment or "",
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        return self.save(fb)

feedback_repository = FeedbackRepository()
