"""
User Session Management Service.
"""

from flask import session
from datetime import datetime
from config import Config

class SessionManager:
    """Manager for Flask User Sessions."""

    @staticmethod
    def create_session(user: dict):
        """Bind user credentials to current HTTP session."""
        session.clear()
        session["user_id"] = user["id"]
        session["user_email"] = user["email"]
        session["user_name"] = user["name"]
        session["user_role"] = user["role"]
        session["logged_in_at"] = datetime.utcnow().isoformat() + "Z"
        session.permanent = True

    @staticmethod
    def clear_session():
        """Clear current session."""
        session.clear()

    @staticmethod
    def is_authenticated() -> bool:
        """Check if current session is active."""
        return "user_id" in session

    @staticmethod
    def get_session_user() -> dict:
        """Get summary dict of session user."""
        if not SessionManager.is_authenticated():
            return None
        return {
            "id": session.get("user_id"),
            "email": session.get("user_email"),
            "name": session.get("user_name"),
            "role": session.get("user_role")
        }

session_manager = SessionManager()
