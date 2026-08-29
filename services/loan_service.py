"""
Loan & EMI Calculator Service
Handles home loans, auto loans, personal loans, monthly EMI calculation, and amortization schedule generation.
"""

import uuid
from datetime import datetime
from typing import List, Dict, Any, Optional
from storage.file_storage import FileStorageEngine
from storage.json_repository import JsonRepository
from finance.tvm_engine import TVMEngine

class LoanService:
    def __init__(self, storage: FileStorageEngine):
        self.repo = JsonRepository(storage, "loans.json", id_field="id")
        self._ensure_sample_loans()

    def _ensure_sample_loans(self):
        loans = self.repo.get_all()
        if not loans:
            sample_loans = [
                ("user_customer_01", "Primary Home Mortgage", "HOME_LOAN", 350000.00, 6.50, 360, 310000.00),
                ("user_customer_01", "Executive Auto Loan", "VEHICLE_LOAN", 35000.00, 5.25, 60, 22500.00),
                ("user_customer_01", "Education Refinance Loan", "EDUCATION_LOAN", 25000.00, 4.75, 120, 14200.00)
            ]
            for u_id, name, l_type, principal, rate, tenure, remaining in sample_loans:
                monthly_rate = (rate / 100.0) / 12.0
                emi = abs(TVMEngine.pmt(monthly_rate, tenure, principal))
                l = {
                    "id": f"loan_{uuid.uuid4().hex[:12]}",
                    "user_id": u_id,
                    "loan_name": name,
                    "loan_type": l_type,
                    "principal_amount": float(principal),
                    "annual_interest_rate": float(rate),
                    "tenure_months": int(tenure),
                    "remaining_balance": float(remaining),
                    "monthly_emi": round(emi, 2),
                    "start_date": "2023-01-01",
                    "created_at": datetime.utcnow().isoformat()
                }
                self.repo.add(l)

    def calculate_emi_details(self, principal: float, rate_annual: float, tenure_months: int) -> Dict[str, Any]:
        r = (rate_annual / 100.0) / 12.0
        emi = abs(TVMEngine.pmt(r, tenure_months, principal)) if r > 0 else (principal / tenure_months)
        total_payment = emi * tenure_months
        total_interest = total_payment - principal
        
        # Generate Amortization Schedule (First 12 months preview)
        schedule = []
        balance = principal
        for m in range(1, tenure_months + 1):
            interest_m = balance * r
            principal_m = emi - interest_m
            balance = max(round(balance - principal_m, 2), 0.0)
            schedule.append({
                "month": m,
                "emi": round(emi, 2),
                "principal_paid": round(principal_m, 2),
                "interest_paid": round(interest_m, 2),
                "remaining_balance": balance
            })
            
        return {
            "principal": round(principal, 2),
            "annual_interest_rate": round(rate_annual, 2),
            "tenure_months": tenure_months,
            "monthly_emi": round(emi, 2),
            "total_interest": round(total_interest, 2),
            "total_payment": round(total_payment, 2),
            "schedule": schedule
        }

    def get_user_loans(self, user_id: str) -> List[Dict[str, Any]]:
        return self.repo.find(lambda l: l.get("user_id") == user_id)
