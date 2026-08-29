"""
Credit Scoring Engine Service
Calculates FICO-like simulated credit score (300-850) based on payment history, utilization, length, and debt ratios.
"""

import uuid
from datetime import datetime
from typing import List, Dict, Any, Optional
from storage.file_storage import FileStorageEngine
from storage.json_repository import JsonRepository

class CreditService:
    def __init__(self, storage: FileStorageEngine):
        self.repo = JsonRepository(storage, "credit_profiles.json", id_field="id")
        self._ensure_sample_profile()

    def _ensure_sample_profile(self):
        profiles = self.repo.get_all()
        if not profiles:
            sample_profile = {
                "id": "cred_user_customer_01",
                "user_id": "user_customer_01",
                "payment_history_pct": 98.5,
                "credit_utilization_pct": 22.4,
                "account_age_years": 6.5,
                "active_lines_of_credit": 5,
                "recent_hard_inquiries": 1,
                "last_updated": datetime.utcnow().isoformat()
            }
            self.repo.add(sample_profile)

    def calculate_credit_score(self, user_id: str) -> Dict[str, Any]:
        profiles = self.repo.find(lambda c: c.get("user_id") == user_id)
        if not profiles:
            p = {
                "payment_history_pct": 95.0,
                "credit_utilization_pct": 30.0,
                "account_age_years": 4.0,
                "active_lines_of_credit": 3,
                "recent_hard_inquiries": 1
            }
        else:
            p = profiles[0]
            
        # 1. Payment History (35% weight -> max 297.5 pts)
        pay_score = (p.get("payment_history_pct", 95.0) / 100.0) * 297.5
        
        # 2. Credit Utilization (30% weight -> max 255 pts)
        util = p.get("credit_utilization_pct", 30.0)
        if util <= 10: util_score = 255.0
        elif util <= 30: util_score = 230.0 - (util - 10) * 2.5
        elif util <= 50: util_score = 180.0 - (util - 30) * 3.0
        else: util_score = max(100.0 - (util - 50) * 2.0, 50.0)
        
        # 3. Credit History Length (15% weight -> max 127.5 pts)
        age = p.get("account_age_years", 4.0)
        age_score = min(age * 15.0, 127.5)
        
        # 4. New Credit / Inquiries (10% weight -> max 85 pts)
        inquiries = p.get("recent_hard_inquiries", 1)
        inquiry_score = max(85.0 - (inquiries * 15.0), 30.0)
        
        # 5. Credit Mix (10% weight -> max 85 pts)
        lines = p.get("active_lines_of_credit", 3)
        mix_score = min(lines * 20.0, 85.0)
        
        total_score = round(300 + pay_score * 0.4 + util_score * 0.4 + age_score * 0.4 + inquiry_score * 0.4 + mix_score * 0.4)
        total_score = min(max(total_score, 300), 850)
        
        if total_score >= 800: category = "EXCELLENT"
        elif total_score >= 740: category = "VERY_GOOD"
        elif total_score >= 670: category = "GOOD"
        elif total_score >= 580: category = "FAIR"
        else: category = "POOR"
        
        return {
            "credit_score": total_score,
            "risk_category": category,
            "payment_history_pct": p.get("payment_history_pct", 98.5),
            "credit_utilization_pct": util,
            "account_age_years": p.get("account_age_years", 6.5),
            "recent_hard_inquiries": inquiries,
            "factors": {
                "Payment History (35%)": round(pay_score, 1),
                "Credit Utilization (30%)": round(util_score, 1),
                "Credit Age (15%)": round(age_score, 1),
                "New Credit (10%)": round(inquiry_score, 1),
                "Credit Mix (10%)": round(mix_score, 1)
            },
            "recommendations": [
                "Keep credit utilization under 30% to maximize your score.",
                "Pay all balances on time; set up automatic payments.",
                "Avoid applying for multiple hard inquiries in short timeframes."
            ]
        }
