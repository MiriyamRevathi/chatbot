"""
Random Forest Classifier Algorithm from Scratch.
"""

import random
from collections import Counter
from nlp.decision_tree import DecisionTreeClassifierSimple

class RandomForestClassifierSimple:
    """Random Forest Ensemble Classifier."""

    def __init__(self, n_estimators=10, max_depth=5):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.trees = []
        self.classes_ = []

    def fit(self, X_vectors: list, y_labels: list):
        self.classes_ = list(set(y_labels))
        n_samples = len(X_vectors)

        for _ in range(self.n_estimators):
            # Bootstrap sample
            indices = [random.randint(0, n_samples - 1) for _ in range(n_samples)]
            X_boot = [X_vectors[i] for i in indices]
            y_boot = [y_labels[i] for i in indices]

            tree = DecisionTreeClassifierSimple(max_depth=self.max_depth)
            tree.fit(X_boot, y_boot)
            self.trees.append(tree)

        return self

    def predict(self, X_vectors: list) -> list:
        tree_preds = [tree.predict(X_vectors) for tree in self.trees]
        final_preds = []
        for i in range(len(X_vectors)):
            sample_votes = [tree_preds[t][i] for t in range(self.n_estimators)]
            most_common = Counter(sample_votes).most_common(1)[0][0]
            final_preds.append(most_common)
        return final_preds
