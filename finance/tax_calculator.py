"""
Federal & State Income Tax Bracket Calculator
Simulates progressive tax bracket calculations, standard deductions, and tax liability estimates.
"""

from typing import Dict, Any

class TaxCalculatorEngine:
    FEDERAL_BRACKETS_SINGLE = [
        (11600, 0.10),
        (47150, 0.12),
        (100525, 0.22),
        (191950, 0.24),
        (243725, 0.32),
        (609350, 0.35),
        (float("inf"), 0.37)
    ]
    STANDARD_DEDUCTION_SINGLE = 14600.0

    @classmethod
    def calculate_federal_tax(cls, gross_annual_income: float, itemized_deductions: float = 0.0) -> Dict[str, Any]:
        deduction = max(cls.STANDARD_DEDUCTION_SINGLE, itemized_deductions)
        taxable_income = max(gross_annual_income - deduction, 0.0)
        
        total_tax = 0.0
        prev_limit = 0.0
        for limit, rate in cls.FEDERAL_BRACKETS_SINGLE:
            if taxable_income > prev_limit:
                taxable_in_bracket = min(taxable_income - prev_limit, limit - prev_limit)
                total_tax += taxable_in_bracket * rate
                prev_limit = limit
            else:
                break
                
        return {
            "gross_income": round(gross_annual_income, 2),
            "deduction_used": round(deduction, 2),
            "taxable_income": round(taxable_income, 2),
            "total_federal_tax": round(total_tax, 2)
        }
