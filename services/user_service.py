"""
User Service Module
Handles registration, authentication, password change, user profile updates, and demo accounts setup.
"""

import uuid
from datetime import datetime
from typing import Optional, Dict, List, Any
from storage.file_storage import FileStorageEngine
from storage.json_repository import JsonRepository
from security.password_hasher import PasswordHasher
from models.user import User

class UserService:
    def __init__(self, storage: FileStorageEngine):
        self.repo = JsonRepository(storage, "users.json", id_field="id")
        self.hasher = PasswordHasher()
        self._ensure_demo_users()

    def _ensure_demo_users(self):
        users = self.repo.get_all()
        if not users:
            demo_users = [
                User(
                    id="user_customer_01",
                    username="customer",
                    email="customer@fintechhub.local",
                    password_hash=self.hasher.hash_password("Customer123!"),
                    role="CUSTOMER",
                    full_name="Alex Mercer (Customer)",
                    phone="+1-555-0192",
                    is_active=True,
                    created_at=datetime.utcnow().isoformat(),
                    updated_at=datetime.utcnow().isoformat()
                ),
                User(
                    id="user_analyst_01",
                    username="analyst",
                    email="analyst@fintechhub.local",
                    password_hash=self.hasher.hash_password("Analyst123!"),
                    role="ANALYST",
                    full_name="Sarah Jenkins (Financial Analyst)",
                    phone="+1-555-0144",
                    is_active=True,
                    created_at=datetime.utcnow().isoformat(),
                    updated_at=datetime.utcnow().isoformat()
                ),
                User(
                    id="user_admin_01",
                    username="admin",
                    email="admin@fintechhub.local",
                    password_hash=self.hasher.hash_password("Admin123!"),
                    role="ADMIN",
                    full_name="David Vance (System Administrator)",
                    phone="+1-555-0100",
                    is_active=True,
                    created_at=datetime.utcnow().isoformat(),
                    updated_at=datetime.utcnow().isoformat()
                )
            ]
            for u in demo_users:
                self.repo.add(u.to_dict())

    def authenticate(self, username_or_email: str, password: str) -> Optional[User]:
        users = self.repo.get_all()
        target = None
        for u in users:
            if u.get("username").lower() == username_or_email.lower() or u.get("email").lower() == username_or_email.lower():
                target = u
                break
        if not target:
            return None
        if not target.get("is_active", True):
            return None
        if self.hasher.verify_password(password, target.get("password_hash")):
            return User.from_dict(target)
        return None

    def register_user(self, username: str, email: str, password: str, full_name: str = "", role: str = "CUSTOMER") -> tuple[Optional[User], str]:
        users = self.repo.get_all()
        for u in users:
            if u.get("username").lower() == username.lower():
                return None, "Username is already registered."
            if u.get("email").lower() == email.lower():
                return None, "Email address is already registered."
        
        is_valid, msg = self.hasher.is_strong_password(password)
        if not is_valid:
            return None, msg

        new_user = User(
            id=f"user_{uuid.uuid4().hex[:12]}",
            username=username,
            email=email,
            password_hash=self.hasher.hash_password(password),
            role=role if role in ["CUSTOMER", "ANALYST", "ADMIN"] else "CUSTOMER",
            full_name=full_name or username.title(),
            is_active=True,
            created_at=datetime.utcnow().isoformat(),
            updated_at=datetime.utcnow().isoformat()
        )
        self.repo.add(new_user.to_dict())
        return new_user, "User registration successful."

    def get_by_id(self, user_id: str) -> Optional[User]:
        data = self.repo.get_by_id(user_id)
        return User.from_dict(data) if data else None

    def get_all_users() -> List[User]:
        return [User.from_dict(d) for d in self.repo.get_all()]

    def update_profile(self, user_id: str, full_name: str, phone: str, email: str) -> tuple[bool, str]:
        user = self.get_by_id(user_id)
        if not user:
            return False, "User not found."
        self.repo.update(user_id, {
            "full_name": full_name,
            "phone": phone,
            "email": email,
            "updated_at": datetime.utcnow().isoformat()
        })
        return True, "Profile updated successfully."

    def change_password(self, user_id: str, old_password: str, new_password: str) -> tuple[bool, str]:
        user = self.get_by_id(user_id)
        if not user:
            return False, "User not found."
        if not self.hasher.verify_password(old_password, user.password_hash):
            return False, "Current password is incorrect."
        is_valid, msg = self.hasher.is_strong_password(new_password)
        if not is_valid:
            return False, msg
        self.repo.update(user_id, {
            "password_hash": self.hasher.hash_password(new_password),
            "updated_at": datetime.utcnow().isoformat()
        })
        return True, "Password updated successfully."
