"""
Tests for Conversation Lifecycle Management.
"""

from repositories.conversation_repository import conversation_repository
from config import Config

def test_conversation_crud():
    conv = conversation_repository.create_conversation("user-99", "CRUD Test")
    assert conv["status"] == Config.STATUS_OPEN
    updated = conversation_repository.update_status(conv["id"], Config.STATUS_RESOLVED)
    assert updated["status"] == Config.STATUS_RESOLVED
