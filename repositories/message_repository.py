"""
Message Repository storing detailed chat logs.
"""

from repositories.base_repository import BaseRepository
from datetime import datetime
import uuid

class MessageRepository(BaseRepository):
    """Repository managing individual chat messages."""

    def __init__(self):
        super().__init__("messages.json")

    def add_message(self, conversation_id: str, sender: str, text: str, metadata: dict = None) -> dict:
        """Add a message record to a conversation."""
        msg = {
            "id": str(uuid.uuid4()),
            "conversation_id": conversation_id,
            "sender": sender,  # "user", "bot", "agent"
            "text": text,
            "metadata": metadata or {},
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        return self.save(msg)

    def get_conversation_messages(self, conversation_id: str) -> list:
        """Retrieve all messages for a specific conversation in chronological order."""
        records = self._read_all()
        msgs = [m for m in records if m.get("conversation_id") == conversation_id]
        return sorted(msgs, key=lambda x: x.get("timestamp", ""))

    def get_recent_messages(self, limit: int = 50) -> list:
        """Get latest messages across system for analytics."""
        records = self._read_all()
        sorted_msgs = sorted(records, key=lambda x: x.get("timestamp", ""), reverse=True)
        return sorted_msgs[:limit]

message_repository = MessageRepository()
