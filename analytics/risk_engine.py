"""
Financial Risk & Health Scoring Engine
Calculates Debt-to-Income (DTI) ratio, Savings ratio, Liquidity buffer, Financial Health Score (0-100), and Risk Category.
"""

from typing import Dict, Any

class FinancialRiskEngine:
    @staticmethod
    def calculate_health_and_risk(
        monthly_income: float,
        monthly_expenses: float,
        total_assets: float,
        total_liabilities: float,
        credit_score: int
    ) -> Dict[str, Any]:
        
        # 1. Debt-to-Income Ratio (DTI)
        dti = (monthly_expenses / monthly_income * 100.0) if monthly_income > 0 else 100.0
        
        # 2. Savings Rate Pct
        savings_rate = max(round(((monthly_income - monthly_expenses) / monthly_income) * 100.0, 1), 0.0) if monthly_income > 0 else 0.0
        
        # 3. Emergency Coverage Months
        coverage_months = round(total_assets / monthly_expenses, 1) if monthly_expenses > 0 else 0.0
        
        # 4. Overall Financial Health Score (0-100)
        # Weights: Savings Rate (30%), DTI (25%), Coverage Months (25%), Credit Score (20%)
        sav_pts = min(savings_rate * 1.5, 30.0)
        dti_pts = max(25.0 - (dti * 0.25), 0.0)
        cov_pts = min(coverage_months * 4.16, 25.0)
        cred_pts = min(((credit_score - 300) / 550.0) * 20.0, 20.0)
        
        health_score = round(sav_pts + dti_pts + cov_pts + cred_pts, 1)
        
        if health_score >= 80: risk_level = "LOW"
        elif health_score >= 60: risk_level = "MODERATE"
        else: risk_level = "HIGH"
        
        return {
            "financial_health_score": health_score,
            "risk_level": risk_level,
            "dti_ratio": round(dti, 1),
            "savings_rate": savings_rate,
            "coverage_months": coverage_months,
            "components": {
                "Savings Rate Contribution": round(sav_pts, 1),
                "Debt-to-Income Contribution": round(dti_pts, 1),
                "Liquidity Buffer Contribution": round(cov_pts, 1),
                "Credit Rating Contribution": round(cred_pts, 1)
            }
        }
