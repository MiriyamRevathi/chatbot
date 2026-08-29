"""
Experiment Repository tracking ML Hyperparameter Runs.
"""

from repositories.base_repository import BaseRepository
from datetime import datetime
import uuid

class ExperimentRepository(BaseRepository):
    """Repository storing ML Experiment Runs."""

    def __init__(self):
        super().__init__("experiments.json")

    def record_experiment(self, name: str, model_type: str, params: dict, metrics: dict, duration_ms: float) -> dict:
        """Save a new ML experiment run."""
        exp = {
            "id": str(uuid.uuid4()),
            "name": name,
            "model_type": model_type,
            "parameters": params,
            "metrics": metrics,
            "duration_ms": duration_ms,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        return self.save(exp)

experiment_repository = ExperimentRepository()
