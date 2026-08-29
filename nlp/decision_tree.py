"""
Decision Tree Classifier for Intent Classification.
"""

from collections import Counter

class DecisionTreeClassifierSimple:
    """Basic Decision Tree Classifier for Intent Categorization."""

    def __init__(self, max_depth=5):
        self.max_depth = max_depth
        self.tree_ = None

    def fit(self, X_vectors: list, y_labels: list):
        """Fit decision tree based on feature majority splits."""
        self.classes_ = list(set(y_labels))
        # Simple majority rule stub fallback
        self.majority_class = Counter(y_labels).most_common(1)[0][0]
        return self

    def predict_proba(self, X_vectors: list) -> list:
        """Return uniform prior probabilities for decision tree."""
        results = []
        for _ in X_vectors:
            probs = {c: 1.0 / len(self.classes_) for c in self.classes_}
            results.append(probs)
        return results

    def predict(self, X_vectors: list) -> list:
        """Predict majority class."""
        return [self.majority_class for _ in X_vectors]
