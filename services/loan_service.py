"""
Loan Service Module
"""
import uuid
from datetime import datetime
from typing import List, Dict, Any
from storage.file_storage import FileStorageEngine
from storage.json_repository import JsonRepository

class LoanService:
    def __init__(self, storage: FileStorageEngine):
        self.repo = JsonRepository(storage, "loans.json", id_field="id")
        self._ensure_sample_loans()

    def _ensure_sample_loans(self):
        loans = self.repo.get_all()
        if not loans:
            sample_loans = [
                ("user_customer_01", "Primary Home Mortgage", "HOME_LOAN", 350000.00, 6.50, 360, 310000.00)
            ]
            for u_id, name, l_type, principal, rate, tenure, remaining in sample_loans:
                l = {
                    "id": f"loan_{uuid.uuid4().hex[:12]}",
                    "user_id": u_id,
                    "loan_name": name,
                    "loan_type": l_type,
                    "principal_amount": float(principal),
                    "annual_interest_rate": float(rate),
                    "tenure_months": int(tenure),
                    "remaining_balance": float(remaining),
                    "monthly_emi": 12500.0,
                    "start_date": "2023-01-01",
                    "created_at": datetime.utcnow().isoformat()
                }
                self.repo.add(l)

    def get_user_loans(self, user_id: str) -> List[Dict[str, Any]]:
        return self.repo.find(lambda l: l.get("user_id") == user_id)

    def add_loan(self, user_id: str, loan_name: str, principal_amount: float, annual_interest_rate: float, tenure_months: int) -> Dict[str, Any]:
        l = {
            "id": f"loan_{uuid.uuid4().hex[:12]}",
            "user_id": user_id,
            "loan_name": loan_name,
            "loan_type": "PERSONAL_LOAN",
            "principal_amount": float(principal_amount),
            "annual_interest_rate": float(annual_interest_rate),
            "tenure_months": int(tenure_months),
            "remaining_balance": float(principal_amount),
            "monthly_emi": round(principal_amount / tenure_months, 2),
            "start_date": datetime.utcnow().strftime("%Y-%m-%d"),
            "created_at": datetime.utcnow().isoformat()
        }
        self.repo.add(l)
        return l
