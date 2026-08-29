"""
Logistic Regression Classifier from Scratch with One-Vs-Rest Scheme.
"""

import math

class LogisticRegressionOVR:
    """Logistic Regression Classifier using Gradient Descent."""

    def __init__(self, lr=0.1, max_iter=100):
        self.lr = lr
        self.max_iter = max_iter
        self.weights_ = {}
        self.biases_ = {}
        self.classes_ = []

    def _sigmoid(self, z):
        return 1.0 / (1.0 + math.exp(-max(-500.0, min(500.0, z))))

    def fit(self, X_vectors: list, y_labels: list):
        """Train One-Vs-Rest Binary Classifiers."""
        self.classes_ = list(set(y_labels))
        n_features = len(X_vectors[0]) if X_vectors else 0

        for c in self.classes_:
            w = [0.0] * n_features
            b = 0.0

            # Create binary target
            y_binary = [1.0 if label == c else 0.0 for label in y_labels]
            N = len(y_binary)

            for _ in range(self.max_iter):
                dw = [0.0] * n_features
                db = 0.0

                for xi, yi in zip(X_vectors, y_binary):
                    z = sum(w[j] * xi[j] for j in range(n_features)) + b
                    pred = self._sigmoid(z)
                    err = pred - yi
                    for j in range(n_features):
                        dw[j] += err * xi[j]
                    db += err

                # Gradient descent step
                for j in range(n_features):
                    w[j] -= self.lr * (dw[j] / N)
                b -= self.lr * (db / N)

            self.weights_[c] = w
            self.biases_[c] = b

        return self

    def predict_proba(self, X_vectors: list) -> list:
        """Compute Softmax probabilities for input vectors."""
        results = []
        for vec in X_vectors:
            scores = {}
            for c in self.classes_:
                w = self.weights_[c]
                b = self.biases_[c]
                z = sum(w[j] * vec[j] for j in range(len(vec))) + b
                scores[c] = self._sigmoid(z)

            total = sum(scores.values()) or 1.0
            probs = {c: round(score / total, 4) for c, score in scores.items()}
            results.append(probs)
        return results

    def predict(self, X_vectors: list) -> list:
        """Predict class label."""
        probas = self.predict_proba(X_vectors)
        return [max(p, key=p.get) for p in probas]
