"""
Customer Segmentation ML Engine
Uses scikit-learn K-Means clustering to profile users into financial personas (Saver, Investor, High Spender, Debt Heavy).
"""

import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from typing import List, Dict, Any

class CustomerSegmentation:
    PERSONAS = {
        0: {"name": "Balanced Wealth Builder", "description": "Moderate spending with steady savings and active index investments."},
        1: {"name": "High Yield Saver", "description": "Low expense ratio with high savings rate and emergency fund buffer."},
        2: {"name": "Aggressive Investor", "description": "High equity allocation, focused on long-term capital appreciation."},
        3: {"name": "High Spender", "description": "Elevated discretionary purchases with lower savings buffer."},
        4: {"name": "Debt Heavy", "description": "Significant loan/credit balances requiring structured debt payoff strategy."}
    }

    def __init__(self, n_clusters: int = 5):
        self.n_clusters = n_clusters
        self.scaler = StandardScaler()
        self.kmeans = KMeans(n_clusters=self.n_clusters, random_state=42, n_init=10)

    def segment_users(self, user_features: List[List[float]]) -> List[Dict[str, Any]]:
        if len(user_features) < self.n_clusters:
            # Fallback for small demo datasets
            results = []
            for i, f in enumerate(user_features):
                cluster_id = i % self.n_clusters
                persona = self.PERSONAS[cluster_id]
                results.append({
                    "cluster_id": cluster_id,
                    "persona_name": persona["name"],
                    "description": persona["description"]
                })
            return results

        X = np.array(user_features)
        X_scaled = self.scaler.fit_transform(X)
        clusters = self.kmeans.fit_predict(X_scaled)

        results = []
        for c in clusters:
            persona = self.PERSONAS.get(c, self.PERSONAS[0])
            results.append({
                "cluster_id": int(c),
                "persona_name": persona["name"],
                "description": persona["description"]
            })

        return results
