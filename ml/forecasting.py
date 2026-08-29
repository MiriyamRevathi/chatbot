"""
Spending Forecasting ML Engine
Uses scikit-learn Ridge Regression to predict next 1-6 months category and total expenses.
"""

import numpy as np
from sklearn.linear_model import Ridge
from typing import List, Dict, Any

class SpendingForecaster:
    @staticmethod
    def forecast_next_months(monthly_totals: List[float], num_months: int = 3) -> List[float]:
        if not monthly_totals:
            return [0.0] * num_months
        if len(monthly_totals) == 1:
            return [round(monthly_totals[0], 2)] * num_months
            
        X = np.array(range(len(monthly_totals))).reshape(-1, 1)
        y = np.array(monthly_totals)
        
        model = Ridge(alpha=1.0)
        model.fit(X, y)
        
        future_X = np.array(range(len(monthly_totals), len(monthly_totals) + num_months)).reshape(-1, 1)
        preds = model.predict(future_X)
        
        return [max(round(float(p), 2), 0.0) for p in preds]
