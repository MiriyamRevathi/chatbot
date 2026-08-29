"""
Administrative Audit Trail Logger Service.
"""

from repositories.audit_repository import audit_repository

class AuditLogger:
    """Audit Logging Helper."""

    @staticmethod
    def log(user_id: str, action: str, details: str = ""):
        """Record audit action."""
        audit_repository.log_action(user_id, action, details)

audit_logger = AuditLogger()
