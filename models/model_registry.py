"""
ML Model Registry Service.
"""

from repositories.model_repository import model_repository

class ModelRegistry:
    """Model Registry managing active production models."""

    @staticmethod
    def get_active_model(model_type: str = "Intent Classification") -> dict:
        """Get current active model record."""
        models = model_repository.get_all()
        for m in models:
            if m.get("type") == model_type and m.get("is_active"):
                return m
        return models[0] if models else None

    @staticmethod
    def activate_model(model_id: str, model_type: str) -> bool:
        """Set specified model as active."""
        return model_repository.set_active_model(model_id, model_type)

model_registry = ModelRegistry()
