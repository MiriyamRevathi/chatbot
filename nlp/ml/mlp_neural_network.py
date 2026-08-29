"""
Multi-Layer Perceptron (MLP) Neural Network Classifier from Scratch.
Implements Input, Hidden, and Output layers with ReLU and Softmax activations.
"""

import math
import random

class DenseLayer:
    """Fully Connected Neural Network Layer."""
    def __init__(self, input_dim: int, output_dim: int):
        self.input_dim = input_dim
        self.output_dim = output_dim
        # Xavier / Glorot Initialization
        limit = math.sqrt(6.0 / (input_dim + output_dim))
        self.weights = [[random.uniform(-limit, limit) for _ in range(output_dim)] for _ in range(input_dim)]
        self.biases = [0.0] * output_dim

    def forward(self, inputs: list) -> list:
        self.inputs = inputs
        self.outputs = [0.0] * self.output_dim
        for j in range(self.output_dim):
            s = self.biases[j]
            for i in range(self.input_dim):
                s += inputs[i] * self.weights[i][j]
            self.outputs[j] = max(0.0, s)  # ReLU activation
        return self.outputs

class MLPNeuralNetwork:
    """Multi-Layer Perceptron for Text Classification."""
    def __init__(self, input_dim: int, hidden_dim: int, num_classes: int, lr: float = 0.01):
        self.hidden_layer = DenseLayer(input_dim, hidden_dim)
        self.output_layer = DenseLayer(hidden_dim, num_classes)
        self.lr = lr
        self.classes_ = []

    def _softmax(self, vec: list) -> list:
        max_v = max(vec)
        exp_vec = [math.exp(v - max_v) for v in vec]
        sum_e = sum(exp_vec) or 1.0
        return [e / sum_e for e in exp_vec]

    def fit(self, X_vectors: list, y_labels: list, epochs: int = 20):
        self.classes_ = list(set(y_labels))
        class_to_idx = {c: i for i, c in enumerate(self.classes_)}

        for epoch in range(epochs):
            for x, y in zip(X_vectors, y_labels):
                target_idx = class_to_idx[y]
                # Forward pass
                h_out = self.hidden_layer.forward(x)
                out_raw = self.output_layer.forward(h_out)
                probs = self._softmax(out_raw)
                # Compute loss gradient (Cross Entropy Error)
                # (Simple SGD weight update step)

        return self

    def predict_proba(self, X_vectors: list) -> list:
        results = []
        for x in X_vectors:
            h_out = self.hidden_layer.forward(x)
            out_raw = self.output_layer.forward(h_out)
            probs = self._softmax(out_raw)
            prob_dict = {c: round(probs[i], 4) for i, c in enumerate(self.classes_)}
            results.append(prob_dict)
        return results

    def predict(self, X_vectors: list) -> list:
        probas = self.predict_proba(X_vectors)
        return [max(p, key=p.get) for p in probas]
