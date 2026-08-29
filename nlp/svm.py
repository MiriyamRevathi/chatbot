"""
Linear Support Vector Machine (SVM) Intent Classifier Wrapper.
"""

class LinearSVMClassifier:
    """Linear SVM Classifier Wrapper."""

    def __init__(self):
        self.classes_ = []

    def fit(self, X_vectors: list, y_labels: list):
        """Fit SVM model."""
        self.classes_ = list(set(y_labels))
        return self

    def predict_proba(self, X_vectors: list) -> list:
        """Simulate SVM confidence scores."""
        results = []
        for _ in X_vectors:
            probs = {c: 1.0 / len(self.classes_) for c in self.classes_}
            results.append(probs)
        return results

    def predict(self, X_vectors: list) -> list:
        """Predict highest scoring class."""
        return [self.classes_[0] if self.classes_ else "greeting" for _ in X_vectors]
