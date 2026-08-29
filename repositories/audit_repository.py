"""
Audit Log Repository tracking System Security Actions.
"""

from repositories.base_repository import BaseRepository
from datetime import datetime
import uuid

class AuditRepository(BaseRepository):
    """Audit Logging Repository."""

    def __init__(self):
        super().__init__("audit_logs.json")

    def log_action(self, user_id: str, action: str, details: str = "") -> dict:
        """Log an administrative or system security action."""
        entry = {
            "id": str(uuid.uuid4()),
            "user_id": user_id,
            "action": action,
            "details": details,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        return self.save(entry)

audit_repository = AuditRepository()
