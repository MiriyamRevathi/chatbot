"""
High-level Authentication Service.
"""

from repositories.user_repository import user_repository
from auth.session_manager import session_manager
from core.validator import Validator
from core.exceptions import AuthenticationError, ValidationError
from repositories.audit_repository import audit_repository

class AuthService:
    """Authentication Service Handling Login, Registration, and Auditing."""

    def login(self, email: str, password: str) -> dict:
        """Authenticate user and set session."""
        if not email or not password:
            raise ValidationError("Email and password are required.")

        user = user_repository.authenticate(email, password)
        if not user:
            raise AuthenticationError("Invalid email or password.")

        session_manager.create_session(user)
        audit_repository.log_action(user["id"], "LOGIN", f"User {user['email']} logged in.")
        return user

    def register(self, email: str, name: str, password: str, role: str = "USER") -> dict:
        """Register a new user account."""
        validated = Validator.validate_registration({
            "email": email,
            "name": name,
            "password": password,
            "role": role
        })

        if user_repository.find_by_email(validated["email"]):
            raise ValidationError("An account with this email already exists.")

        user = user_repository.create_user(
            email=validated["email"],
            name=validated["name"],
            role=validated["role"],
            password=validated["password"]
        )

        session_manager.create_session(user)
        audit_repository.log_action(user["id"], "REGISTER", f"User {user['email']} registered as {user['role']}.")
        return user

    def logout(self):
        """Logout user and record audit log."""
        user = session_manager.get_session_user()
        if user:
            audit_repository.log_action(user["id"], "LOGOUT", f"User {user['email']} logged out.")
        session_manager.clear_session()

auth_service = AuthService()
