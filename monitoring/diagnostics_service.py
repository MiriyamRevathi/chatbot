"""
Diagnostics Service backing the /diagnostics Endpoint.
"""

from monitoring.health_checker import health_checker
from repositories.user_repository import user_repository
from repositories.conversation_repository import conversation_repository
from repositories.model_repository import model_repository

class DiagnosticsService:
    """Service serving comprehensive system telemetry."""

    def get_diagnostics(self) -> dict:
        """Gather full system diagnostic metrics."""
        health = health_checker.get_system_health()
        users_count = len(user_repository.get_all())
        convs_count = len(conversation_repository.get_all())
        models_count = len(model_repository.get_all())

        return {
            "health": health,
            "telemetry": {
                "total_users": users_count,
                "total_conversations": convs_count,
                "registered_models": models_count,
                "flask_status": "RUNNING",
                "ml_engine_status": "OPERATIONAL"
            }
        }

diagnostics_service = DiagnosticsService()
