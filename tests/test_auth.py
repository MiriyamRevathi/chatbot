"""
Tests for Authentication & Password Hashing.
"""

from auth.password_hasher import password_hasher
from auth.auth_service import auth_service
from repositories.user_repository import user_repository

def test_password_hashing():
    pwd = "SecretPass123!"
    hashed = password_hasher.hash(pwd)
    assert hashed != pwd
    assert password_hasher.verify(pwd, hashed) is True
    assert password_hasher.verify("WrongPass", hashed) is False

def test_demo_accounts():
    user = user_repository.find_by_email("admin@chatflow.local")
    assert user is not None
    assert user["role"] == "ADMIN"
