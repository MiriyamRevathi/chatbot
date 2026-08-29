"""
High-Level Experiment Tracking Service.
"""

from repositories.experiment_repository import experiment_repository
from experiments.run_logger import run_logger

class ExperimentService:
    """High level service managing ML experiments."""

    def create_experiment(self, name: str, model_type: str, params: dict, metrics: dict, duration_ms: float) -> dict:
        """Create new experiment record."""
        return run_logger.log_run(name, model_type, params, metrics, duration_ms)

    def list_experiments(self) -> list:
        """Retrieve all experiment runs."""
        return experiment_repository.get_all()

experiment_service = ExperimentService()
