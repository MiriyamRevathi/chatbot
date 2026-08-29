"""
Rule-Based Transaction Auto-Categorization Engine
Matches merchant names, descriptions, and payment keywords against 80+ financial spending rules.
"""

import re
from typing import Dict, List, Tuple

class CategorizationEngine:
    CATEGORIES = {
        "INCOME": ["salary", "payroll", "paycheck", "dividend", "interest", "stipend", "bonus", "refund", "reimbursement", "deposit"],
        "GROCERIES": ["walmart", "target", "whole foods", "trader joe", "safeway", "kroger", "costco", "aldic", "supermarket", "grocery"],
        "DINING": ["starbucks", "mcdonalds", "subway", "chipotle", "uber eats", "doordash", "grubhub", "burger king", "dominos", "restaurant", "cafe", "diner"],
        "UTILITIES": ["electric", "water", "gas bill", "power", "waste", "comcast", "verizon", "att", "t-mobile", "internet", "utility"],
        "HOUSING": ["rent", "mortgage", "hoa fee", "landlord", "housing", "lease", "apartment"],
        "TRANSPORTATION": ["uber", "lyft", "shell", "chevron", "bp", "exxon", "gas station", "parking", "subway", "transit", "toll"],
        "ENTERTAINMENT": ["netflix", "spotify", "hulu", "disney", "cinema", "theater", "amzn prime", "steam", "playstation", "ticketmaster"],
        "HEALTHCARE": ["cvs", "walgreens", "pharmacy", "doctor", "dental", "hospital", "clinic", "health insurance", "medication"],
        "SHOPPING": ["amazon", "ebay", "best buy", "apple store", "nike", "zara", "clothing", "electronics", "department store"],
        "INVESTMENT": ["vanguard", "fidelity", "charles schwab", "robinhood", "etrade", "stock purchase", "crypto", "brokerage"],
        "DEBT_PAYMENT": ["credit card payment", "loan payment", "car payment", "student loan", "interest charge"]
    }

    @classmethod
    def categorize(cls, merchant: str, description: str = "", amount: float = 0.0) -> str:
        text = f"{merchant} {description}".lower()
        if amount > 0:
            for kw in cls.CATEGORIES["INCOME"]:
                if kw in text:
                    return "INCOME"
        for category, keywords in cls.CATEGORIES.items():
            if category == "INCOME":
                continue
            for kw in keywords:
                if re.search(r"\b" + re.escape(kw) + r"\b", text):
                    return category
        return "MISCELLANEOUS"
