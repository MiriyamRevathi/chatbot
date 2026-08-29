"""
ML Classification Metrics Calculator.
Computes Accuracy, Precision, Recall, F1 Score, and Confusion Matrix.
"""

from collections import defaultdict

class MetricsCalculator:
    """Evaluator computing standard classification metrics."""

    @staticmethod
    def evaluate(y_true: list, y_pred: list) -> dict:
        """Compute Accuracy, Precision, Recall, F1 score, and Confusion Matrix."""
        if not y_true or not y_pred or len(y_true) != len(y_pred):
            return {"accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1_score": 0.0, "confusion_matrix": {}}

        total = len(y_true)
        correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
        accuracy = round(correct / total, 4)

        classes = sorted(list(set(y_true).union(set(y_pred))))
        cm = {c1: {c2: 0 for c2 in classes} for c1 in classes}

        for t, p in zip(y_true, y_pred):
            cm[t][p] += 1

        precisions = []
        recalls = []

        for c in classes:
            tp = cm[c][c]
            fp = sum(cm[other][c] for other in classes if other != c)
            fn = sum(cm[c][other] for other in classes if other != c)

            precision_c = tp / (tp + fp) if (tp + fp) > 0 else 0.0
            recall_c = tp / (tp + fn) if (tp + fn) > 0 else 0.0

            precisions.append(precision_c)
            recalls.append(recall_c)

        macro_precision = round(sum(precisions) / len(classes), 4) if classes else 0.0
        macro_recall = round(sum(recalls) / len(classes), 4) if classes else 0.0

        if (macro_precision + macro_recall) > 0:
            f1_score = round(2 * (macro_precision * macro_recall) / (macro_precision + macro_recall), 4)
        else:
            f1_score = 0.0

        return {
            "accuracy": accuracy,
            "precision": macro_precision,
            "recall": macro_recall,
            "f1_score": f1_score,
            "confusion_matrix": cm
        }

metrics_calculator = MetricsCalculator()
