"""
Cosine Similarity Math Module.
"""

import math

class CosineSimilarity:
    """Compute Cosine Similarity between vector pairs."""

    @staticmethod
    def compute(v1: list, v2: list) -> float:
        """Compute cosine similarity dot product."""
        if not v1 or not v2 or len(v1) != len(v2):
            return 0.0

        dot = sum(a * b for a, b in zip(v1, v2))
        norm1 = math.sqrt(sum(a * a for a in v1))
        norm2 = math.sqrt(sum(b * b for b in v2))

        if norm1 == 0.0 or norm2 == 0.0:
            return 0.0

        return round(dot / (norm1 * norm2), 4)

cosine_similarity = CosineSimilarity()
