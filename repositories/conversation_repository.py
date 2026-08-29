"""
Conversation Repository for Managing Multi-Turn Chat Sessions.
"""

from repositories.base_repository import BaseRepository
from datetime import datetime
from config import Config
import uuid

class ConversationRepository(BaseRepository):
    """Repository storing conversation metadata and lifecycle states."""

    def __init__(self):
        super().__init__("conversations.json")

    def create_conversation(self, user_id: str, title: str = "New Conversation") -> dict:
        """Initialize a new conversation session."""
        conv = {
            "id": str(uuid.uuid4()),
            "user_id": user_id,
            "title": title,
            "status": Config.STATUS_OPEN,
            "tags": [],
            "message_count": 0,
            "created_at": datetime.utcnow().isoformat() + "Z",
            "updated_at": datetime.utcnow().isoformat() + "Z",
            "assigned_agent_id": None,
            "internal_notes": ""
        }
        return self.save(conv)

    def get_user_conversations(self, user_id: str) -> list:
        """Retrieve all conversations belonging to a specific user."""
        records = self._read_all()
        user_convs = [c for c in records if c.get("user_id") == user_id]
        return sorted(user_convs, key=lambda x: x.get("updated_at", ""), reverse=True)

    def search_conversations(self, query: str, user_id: str = None) -> list:
        """Search conversations by title or tags."""
        records = self._read_all()
        q = query.lower()
        results = []
        for c in records:
            if user_id and c.get("user_id") != user_id:
                continue
            if q in c.get("title", "").lower() or any(q in t.lower() for t in c.get("tags", [])):
                results.append(c)
        return results

    def update_status(self, conv_id: str, status: str, agent_id: str = None) -> dict:
        """Update status (OPEN, ACTIVE, RESOLVED, ESCALATED, ARCHIVED)."""
        conv = self.find_by_id(conv_id)
        if conv:
            conv["status"] = status
            conv["updated_at"] = datetime.utcnow().isoformat() + "Z"
            if agent_id:
                conv["assigned_agent_id"] = agent_id
            return self.save(conv)
        return None

    def add_note(self, conv_id: str, note: str) -> dict:
        """Add internal agent note."""
        conv = self.find_by_id(conv_id)
        if conv:
            existing = conv.get("internal_notes", "")
            timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
            conv["internal_notes"] = f"{existing}\n[{timestamp}] {note}".strip()
            return self.save(conv)
        return None

conversation_repository = ConversationRepository()
