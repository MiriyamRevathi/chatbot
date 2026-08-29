"""
Model Comparison and Cross-Validation Evaluator.
"""

from models.metrics import metrics_calculator

class ModelEvaluator:
    """Evaluator comparing multiple candidate ML models."""

    @staticmethod
    def compare_models(model_results: list) -> dict:
        """Compare performance metrics across multiple models."""
        sorted_models = sorted(model_results, key=lambda x: x.get("f1_score", 0.0), reverse=True)
        best = sorted_models[0] if sorted_models else None
        return {
            "best_model": best,
            "leaderboard": sorted_models
        }

model_evaluator = ModelEvaluator()
