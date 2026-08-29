"""
Human Escalation Manager.
Manages priority queues for support agent takeover.
"""

from repositories.conversation_repository import conversation_repository
from config import Config

class EscalationManager:
    """Human Agent Escalation Manager."""

    def escalate_conversation(self, conversation_id: str, reason: str = "Low bot confidence") -> dict:
        """Escalate conversation to agent queue."""
        conv = conversation_repository.update_status(conversation_id, Config.STATUS_ESCALATED)
        if conv:
            conversation_repository.add_note(conversation_id, f"Escalated to human support queue: {reason}")
        return conv

escalation_manager = EscalationManager()
