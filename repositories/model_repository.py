"""
ML Model Repository managing Model Artifact Metadata.
"""

from repositories.base_repository import BaseRepository
from datetime import datetime
import uuid

class ModelRepository(BaseRepository):
    """Repository tracking trained ML models."""

    def __init__(self):
        super().__init__("models.json")
        self.init_default_models()

    def init_default_models(self):
        """Seed baseline model records."""
        if not self._read_all():
            default_models = [
                {
                    "id": "model-intent-naive-bayes-v1",
                    "name": "Multinomial Naive Bayes Intent Classifier",
                    "type": "Intent Classification",
                    "algorithm": "Naive Bayes",
                    "version": "1.0.0",
                    "accuracy": 0.925,
                    "f1_score": 0.918,
                    "is_active": True,
                    "artifact_path": "artifacts/intent_nb_v1.joblib",
                    "created_at": datetime.utcnow().isoformat() + "Z"
                },
                {
                    "id": "model-intent-logistic-regression-v1",
                    "name": "Logistic Regression Intent Classifier",
                    "type": "Intent Classification",
                    "algorithm": "Logistic Regression",
                    "version": "1.0.0",
                    "accuracy": 0.942,
                    "f1_score": 0.939,
                    "is_active": False,
                    "artifact_path": "artifacts/intent_logreg_v1.joblib",
                    "created_at": datetime.utcnow().isoformat() + "Z"
                },
                {
                    "id": "model-sentiment-vader-hybrid-v1",
                    "name": "Lexicon-Hybrid Sentiment Engine",
                    "type": "Sentiment Analysis",
                    "algorithm": "Lexicon + Logistic Regression",
                    "version": "1.0.0",
                    "accuracy": 0.898,
                    "f1_score": 0.892,
                    "is_active": True,
                    "artifact_path": "artifacts/sentiment_hybrid_v1.joblib",
                    "created_at": datetime.utcnow().isoformat() + "Z"
                }
            ]
            for m in default_models:
                self.save(m)

    def set_active_model(self, model_id: str, model_type: str) -> bool:
        """Activate a specific model for a task type."""
        records = self._read_all()
        for r in records:
            if r.get("type") == model_type:
                r["is_active"] = (r.get("id") == model_id)
        self._write_all(records)
        return True

model_repository = ModelRepository()
