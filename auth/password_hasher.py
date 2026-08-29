"""
Password Hashing and Salt Management Service.
"""

from core.security import hash_password, verify_password

class PasswordHasher:
    """Password Hashing Manager."""

    @staticmethod
    def hash(password: str) -> str:
        """Hash plain password."""
        return hash_password(password)

    @staticmethod
    def verify(password: str, hashed_hex: str) -> bool:
        """Verify plain password against stored hash."""
        return verify_password(password, hashed_hex)

password_hasher = PasswordHasher()
