"""
Tests for REST API Endpoints.
"""

import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_api_health(client):
    res = client.get("/api/health")
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "HEALTHY"

def test_api_diagnostics(client):
    res = client.get("/api/diagnostics")
    assert res.status_code == 200
    data = res.get_json()
    assert "telemetry" in data
