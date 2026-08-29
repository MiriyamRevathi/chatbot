"""
Experiment Metrics Comparator.
"""

class MetricsComparator:
    """Compares metrics between experiment runs."""

    @staticmethod
    def compare(exp1: dict, exp2: dict) -> dict:
        """Compute delta difference between two experiment runs."""
        m1 = exp1.get("metrics", {})
        m2 = exp2.get("metrics", {})
        return {
            "accuracy_delta": round(m2.get("accuracy", 0) - m1.get("accuracy", 0), 4),
            "f1_delta": round(m2.get("f1_score", 0) - m1.get("f1_score", 0), 4)
        }

metrics_comparator = MetricsComparator()
