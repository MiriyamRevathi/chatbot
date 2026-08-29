"""
Tests for Model Trainer & Evaluation Metrics.
"""

from models.metrics import metrics_calculator
from models.trainer import model_trainer

def test_metrics_calculator():
    y_true = ["cat", "dog", "cat"]
    y_pred = ["cat", "dog", "dog"]
    metrics = metrics_calculator.evaluate(y_true, y_pred)
    assert "accuracy" in metrics
    assert "f1_score" in metrics

def test_model_trainer():
    model_record = model_trainer.train_intent_model("naive_bayes", "Pytest Model")
    assert model_record["algorithm"] == "naive_bayes"
    assert model_record["accuracy"] > 0.0
