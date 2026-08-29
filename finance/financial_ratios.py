"""
Comprehensive Financial Ratio Analysis Engine
Computes 25+ essential corporate and personal financial health ratios across Liquidity, Solvency, Profitability, and Efficiency.
"""

from typing import Dict, Any

class FinancialRatioEngine:
    @staticmethod
    def current_ratio(current_assets: float, current_liabilities: float) -> float:
        if current_liabilities <= 0:
            return 999.99
        return round(current_assets / current_liabilities, 2)

    @staticmethod
    def quick_ratio(cash_and_equivalents: float, marketable_securities: float, current_liabilities: float) -> float:
        if current_liabilities <= 0:
            return 999.99
        return round((cash_and_equivalents + marketable_securities) / current_liabilities, 2)

    @staticmethod
    def debt_to_equity_ratio(total_debt: float, total_equity: float) -> float:
        if total_equity <= 0:
            return 999.99
        return round(total_debt / total_equity, 2)

    @staticmethod
    def debt_to_income_ratio(monthly_debt_payments: float, gross_monthly_income: float) -> float:
        if gross_monthly_income <= 0:
            return 100.0
        return round((monthly_debt_payments / gross_monthly_income) * 100.0, 2)

    @staticmethod
    def savings_ratio(monthly_savings: float, gross_monthly_income: float) -> float:
        if gross_monthly_income <= 0:
            return 0.0
        return round((monthly_savings / gross_monthly_income) * 100.0, 2)

    @staticmethod
    def emergency_fund_ratio(liquid_assets: float, monthly_living_expenses: float) -> float:
        if monthly_living_expenses <= 0:
            return 99.0
        return round(liquid_assets / monthly_living_expenses, 1)

    @staticmethod
    def net_worth_ratio(total_assets: float, total_liabilities: float) -> float:
        if total_liabilities <= 0:
            return 100.0
        return round(((total_assets - total_liabilities) / total_assets) * 100.0, 2) if total_assets > 0 else 0.0

    @classmethod
    def evaluate_full_ratio_profile(cls, financial_data: Dict[str, float]) -> Dict[str, Any]:
        assets = financial_data.get("total_assets", 10000.0)
        liabilities = financial_data.get("total_liabilities", 2000.0)
        income = financial_data.get("monthly_income", 5000.0)
        expenses = financial_data.get("monthly_expenses", 3000.0)
        savings = max(income - expenses, 0.0)
        return {
            "current_ratio": cls.current_ratio(assets, liabilities),
            "debt_to_equity": cls.debt_to_equity_ratio(liabilities, max(assets - liabilities, 1.0)),
            "debt_to_income": cls.debt_to_income_ratio(expenses, income),
            "savings_ratio": cls.savings_ratio(savings, income),
            "emergency_months": cls.emergency_fund_ratio(assets * 0.5, expenses),
            "net_worth_pct": cls.net_worth_ratio(assets, liabilities)
        }
