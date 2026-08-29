"""
Password Hashing and Verification Module
Uses Werkzeug security helpers for pbkdf2/scrypt password hashing.
"""

from werkzeug.security import generate_password_hash, check_password_hash
import re

class PasswordHasher:
    @staticmethod
    def hash_password(password: str) -> str:
        return generate_password_hash(password, method="scrypt")

    @staticmethod
    def verify_password(password: str, password_hash: str) -> bool:
        return check_password_hash(password_hash, password)

    @staticmethod
    def is_strong_password(password: str) -> tuple[bool, str]:
        if len(password) < 8:
            return False, "Password must be at least 8 characters long."
        if not re.search(r"[A-Z]", password):
            return False, "Password must contain at least one uppercase letter."
        if not re.search(r"[a-z]", password):
            return False, "Password must contain at least one lowercase letter."
        if not re.search(r"[0-9]", password):
            return False, "Password must contain at least one digit."
        return True, "Password meets security strength requirements."
