"""
ML Model Training Pipeline.
"""

import time
import os
import joblib
from config import Config
from nlp.intent_classifier import IntentClassifier
from models.metrics import metrics_calculator
from repositories.model_repository import model_repository

class ModelTrainer:
    """Trainer executing ML training jobs and exporting joblib artifacts."""

    def train_intent_model(self, algorithm: str = "naive_bayes", name: str = "Custom Intent Classifier") -> dict:
        """Train intent classifier and save joblib artifact."""
        start_time = time.time()

        classifier = IntentClassifier(model_type=algorithm)

        duration = round((time.time() - start_time) * 1000, 2)

        # Generate mock evaluation labels
        y_true = ["greeting", "billing", "password", "order_status", "refund"] * 10
        y_pred = classifier.model.predict(classifier.vectorizer.transform(y_true))
        metrics = metrics_calculator.evaluate(y_true, y_pred)

        artifact_name = f"intent_{algorithm}_{int(time.time())}.joblib"
        artifact_path = os.path.join(Config.ARTIFACTS_DIR, artifact_name)

        # Save model via joblib
        joblib.dump(classifier, artifact_path)

        model_record = {
            "id": f"model-custom-{int(time.time())}",
            "name": name,
            "type": "Intent Classification",
            "algorithm": algorithm,
            "version": "1.0.0",
            "accuracy": metrics["accuracy"],
            "f1_score": metrics["f1_score"],
            "is_active": False,
            "artifact_path": artifact_path,
            "training_time_ms": duration
        }
        model_repository.save(model_record)
        return model_record

model_trainer = ModelTrainer()
