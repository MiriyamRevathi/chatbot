"""
Single-Layer Perceptron Classifier.
"""

class PerceptronClassifier:
    """Binary/Multi-class Single Layer Perceptron."""

    def __init__(self, lr=0.01, epochs=10):
        self.lr = lr
        self.epochs = epochs
        self.weights = {}
        self.biases = {}

    def fit(self, X_vectors: list, y_labels: list):
        self.classes_ = list(set(y_labels))
        n_features = len(X_vectors[0]) if X_vectors else 0

        for c in self.classes_:
            w = [0.0] * n_features
            b = 0.0
            for _ in range(self.epochs):
                for x, y in zip(X_vectors, y_labels):
                    target = 1.0 if y == c else -1.0
                    score = sum(w[i] * x[i] for i in range(n_features)) + b
                    pred = 1.0 if score >= 0 else -1.0
                    if pred != target:
                        update = self.lr * target
                        for i in range(n_features):
                            w[i] += update * x[i]
                        b += update
            self.weights[c] = w
            self.biases[c] = b
        return self
