"""
Security Utilities: Password Hashing, Input Sanitization, Token Generation.
"""

import hashlib
import hmac
import secrets
import html
import re
from config import Config

def hash_password(password: str) -> str:
    """Generate secure salted SHA-256 hash."""
    salt = Config.SECURITY_PASSWORD_SALT.encode("utf-8")
    pwd_bytes = password.encode("utf-8")
    hashed = hashlib.pbkdf2_hmac("sha256", pwd_bytes, salt, 100000)
    return hashed.hex()

def verify_password(password: str, hashed_hex: str) -> bool:
    """Verify password against stored hash."""
    computed_hex = hash_password(password)
    return hmac.compare_digest(computed_hex, hashed_hex)

def sanitize_input(text: str) -> str:
    """Sanitize user text input to prevent XSS."""
    if not isinstance(text, str):
        return ""
    # Strip dangerous HTML script tags
    cleaned = html.escape(text.strip())
    return cleaned

def generate_token(length=32) -> str:
    """Generate a crypto-secure URL-safe token."""
    return secrets.token_urlsafe(length)

def is_valid_email(email: str) -> bool:
    """Validate email address format."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email.strip())) if email else False
