"""
K-Nearest Neighbors (KNN) Classifier from Scratch.
"""

import math
from collections import Counter

class KNNClassifier:
    """K-Nearest Neighbors Classifier with Euclidean Distance."""

    def __init__(self, k=3):
        self.k = k
        self.X_train = []
        self.y_train = []

    def fit(self, X_vectors: list, y_labels: list):
        self.X_train = X_vectors
        self.y_train = y_labels
        self.classes_ = list(set(y_labels))
        return self

    def _euclidean_distance(self, v1: list, v2: list) -> float:
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))

    def predict(self, X_vectors: list) -> list:
        predictions = []
        for vec in X_vectors:
            distances = []
            for idx, train_vec in enumerate(self.X_train):
                dist = self._euclidean_distance(vec, train_vec)
                distances.append((dist, self.y_train[idx]))

            sorted_k = sorted(distances, key=lambda x: x[0])[:self.k]
            k_labels = [label for _, label in sorted_k]
            most_common = Counter(k_labels).most_common(1)[0][0]
            predictions.append(most_common)
        return predictions
