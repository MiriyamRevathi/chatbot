"""
Multinomial Naive Bayes Classifier from Scratch.
"""

import math
from collections import defaultdict

class MultinomialNaiveBayes:
    """Multinomial Naive Bayes Intent Classifier with Laplace Smoothing."""

    def __init__(self, alpha=1.0):
        self.alpha = alpha
        self.classes_ = []
        self.class_priors_ = {}
        self.feature_probs_ = {}
        self.vocab_size_ = 0

    def fit(self, X_vectors: list, y_labels: list, feature_names: list):
        """Fit Naive Bayes on training vectors."""
        self.classes_ = list(set(y_labels))
        self.vocab_size_ = len(feature_names)
        N = len(y_labels)

        class_counts = defaultdict(int)
        feature_counts = defaultdict(lambda: [0.0] * self.vocab_size_)
        class_total_tokens = defaultdict(float)

        for vec, label in zip(X_vectors, y_labels):
            class_counts[label] += 1
            for f_idx, val in enumerate(vec):
                feature_counts[label][f_idx] += val
                class_total_tokens[label] += val

        # Calculate class log priors and feature log probabilities
        for c in self.classes_:
            self.class_priors_[c] = math.log(class_counts[c] / N)
            self.feature_probs_[c] = []
            denom = class_total_tokens[c] + self.alpha * self.vocab_size_

            for f_idx in range(self.vocab_size_):
                num = feature_counts[c][f_idx] + self.alpha
                self.feature_probs_[c].append(math.log(num / denom))

        return self

    def predict_proba(self, X_vectors: list) -> list:
        """Compute class probabilities for test samples."""
        probabilities = []
        for vec in X_vectors:
            scores = {}
            for c in self.classes_:
                log_prob = self.class_priors_[c]
                for f_idx, val in enumerate(vec):
                    if val > 0:
                        log_prob += val * self.feature_probs_[c][f_idx]
                scores[c] = log_prob

            # Convert log probabilities to normalized probabilities via Softmax
            max_score = max(scores.values())
            exp_scores = {c: math.exp(score - max_score) for c, score in scores.items()}
            sum_exp = sum(exp_scores.values())
            norm_probs = {c: round(exp / sum_exp, 4) for c, exp in exp_scores.items()}
            probabilities.append(norm_probs)
        return probabilities

    def predict(self, X_vectors: list) -> list:
        """Predict highest probability class for samples."""
        probas = self.predict_proba(X_vectors)
        return [max(p, key=p.get) for p in probas]
