"""
Experiment Run Logger.
"""

from repositories.experiment_repository import experiment_repository

class RunLogger:
    """Logs individual experiment runs."""

    @staticmethod
    def log_run(name: str, model_type: str, params: dict, metrics: dict, duration_ms: float) -> dict:
        """Record experiment run parameters and output metrics."""
        return experiment_repository.record_experiment(name, model_type, params, metrics, duration_ms)

run_logger = RunLogger()
