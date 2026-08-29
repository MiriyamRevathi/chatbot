"""
ML Anomaly Fraud Detection Engine
Uses scikit-learn Isolation Forest and Local Outlier Factor (LOF) models to detect transaction fraud.
"""

import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from datetime import datetime
from typing import List, Dict, Any, Tuple

class MLFraudDetector:
    def __init__(self, contamination: float = 0.05):
        self.contamination = contamination
        self.iso_forest = IsolationForest(contamination=self.contamination, random_state=42)
        self.lof = LocalOutlierFactor(n_neighbors=5, contamination=self.contamination, novelty=True)

    def extract_features(self, transactions: List[Dict[str, Any]]) -> np.ndarray:
        features = []
        for t in transactions:
            amt = abs(float(t.get("amount", 0.0)))
            dt_str = t.get("transaction_date", "2026-08-01")
            try:
                dt = datetime.strptime(dt_str, "%Y-%m-%d")
                day_of_week = dt.weekday()
            except:
                day_of_week = 0
            
            # Simple category encoding index
            cat = t.get("category", "MISCELLANEOUS").upper()
            cat_idx = hash(cat) % 10
            
            features.append([amt, day_of_week, cat_idx])
            
        return np.array(features) if features else np.empty((0, 3))

    def train_and_predict(self, transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        if len(transactions) < 5:
            for t in transactions:
                t["is_flagged_fraud"] = False
                t["anomaly_score"] = 0.05
                t["risk_level"] = "LOW"
            return transactions

        X = self.extract_features(transactions)
        self.iso_forest.fit(X)
        scores = -self.iso_forest.score_samples(X)  # Higher means more anomalous
        predictions = self.iso_forest.predict(X)    # -1 for anomaly, 1 for normal

        for i, t in enumerate(transactions):
            score = round(float(scores[i]), 3)
            is_anomaly = bool(predictions[i] == -1) or (abs(t.get("amount", 0.0)) > 5000.0)
            
            t["is_flagged_fraud"] = is_anomaly
            t["anomaly_score"] = score
            t["risk_level"] = "HIGH" if is_anomaly else ("MEDIUM" if score > 0.55 else "LOW")
            
        return transactions
