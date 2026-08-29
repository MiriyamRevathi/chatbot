"""
User Repository for User Management and RBAC Storage.
"""

from repositories.base_repository import BaseRepository
from core.security import hash_password, verify_password
from config import Config
from datetime import datetime
import uuid

class UserRepository(BaseRepository):
    """User Repository managing credentials and user profiles."""

    def __init__(self):
        super().__init__("users.json")
        self.init_demo_users()

    def init_demo_users(self):
        """Seed demo accounts if missing."""
        users = self._read_all()
        if not users:
            for demo in Config.DEMO_ACCOUNTS:
                self.create_user(
                    email=demo["email"],
                    name=demo["name"],
                    role=demo["role"],
                    password=demo["password"]
                )

    def create_user(self, email: str, name: str, role: str, password: str) -> dict:
        """Create a new user account."""
        email_clean = email.strip().lower()
        if self.find_by_email(email_clean):
            return None

        user = {
            "id": str(uuid.uuid4()),
            "email": email_clean,
            "name": name.strip(),
            "role": role.strip(),
            "password_hash": hash_password(password),
            "is_active": True,
            "created_at": datetime.utcnow().isoformat() + "Z",
            "last_login": None
        }
        return self.save(user)

    def find_by_email(self, email: str) -> dict:
        """Locate user record by email."""
        if not email:
            return None
        email_clean = email.strip().lower()
        users = self._read_all()
        for u in users:
            if u.get("email") == email_clean:
                return u
        return None

    def authenticate(self, email: str, password: str) -> dict:
        """Verify user credentials."""
        user = self.find_by_email(email)
        if not user or not user.get("is_active"):
            return None
        if verify_password(password, user.get("password_hash")):
            user["last_login"] = datetime.utcnow().isoformat() + "Z"
            self.save(user)
            return user
        return None

    def update_role(self, user_id: str, new_role: str) -> bool:
        """Update role of a user."""
        user = self.find_by_id(user_id)
        if user:
            user["role"] = new_role
            self.save(user)
            return True
        return False

    def toggle_active(self, user_id: str) -> bool:
        """Toggle user active status."""
        user = self.find_by_id(user_id)
        if user:
            user["is_active"] = not user.get("is_active", True)
            self.save(user)
            return True
        return False

user_repository = UserRepository()
