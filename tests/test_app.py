"""
Tests for Flask Application Factory & Error Handlers.
"""

import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config.update({"TESTING": True, "SECRET_KEY": "test-key"})
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_app_creation(app):
    assert app is not None
    assert app.testing is True

def test_404_route(client):
    res = client.get("/non-existent-route-123")
    assert res.status_code == 404
