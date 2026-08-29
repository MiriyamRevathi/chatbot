"""
Budget Planning & Spending Velocity Service
Manages category spending limits, monthly budgets, progress tracking, and overspending triggers.
"""

import uuid
from datetime import datetime
from typing import List, Dict, Any, Optional
from storage.file_storage import FileStorageEngine
from storage.json_repository import JsonRepository
from services.transaction_service import TransactionService

class BudgetService:
    def __init__(self, storage: FileStorageEngine):
        self.storage = storage
        self.repo = JsonRepository(storage, "budgets.json", id_field="id")
        self._ensure_sample_budgets()

    def _ensure_sample_budgets(self):
        budgets = self.repo.get_all()
        if not budgets:
            sample_budgets = [
                ("user_customer_01", "GROCERIES", 600.00, "2026-08"),
                ("user_customer_01", "DINING", 300.00, "2026-08"),
                ("user_customer_01", "UTILITIES", 250.00, "2026-08"),
                ("user_customer_01", "HOUSING", 1500.00, "2026-08"),
                ("user_customer_01", "TRANSPORTATION", 200.00, "2026-08"),
                ("user_customer_01", "ENTERTAINMENT", 150.00, "2026-08"),
                ("user_customer_01", "SHOPPING", 400.00, "2026-08")
            ]
            for u_id, cat, limit, period in sample_budgets:
                b = {
                    "id": f"bgt_{uuid.uuid4().hex[:12]}",
                    "user_id": u_id,
                    "category": cat,
                    "limit_amount": float(limit),
                    "period": period,
                    "created_at": datetime.utcnow().isoformat()
                }
                self.repo.add(b)

    def get_user_budgets_with_progress(self, user_id: str, period: str = "2026-08") -> List[Dict[str, Any]]:
        budgets = self.repo.find(lambda b: b.get("user_id") == user_id and b.get("period") == period)
        tx_service = TransactionService(self.storage)
        category_spending = tx_service.get_category_breakdown(user_id)
        
        results = []
        for b in budgets:
            cat = b.get("category")
            limit = b.get("limit_amount", 1.0)
            spent = category_spending.get(cat, 0.0)
            remaining = round(limit - spent, 2)
            pct = min(round((spent / limit) * 100, 1), 100.0) if limit > 0 else 0.0
            status = "HEALTHY" if pct < 85 else ("WARNING" if pct < 100 else "EXCEEDED")
            results.append({
                "id": b.get("id"),
                "category": cat,
                "limit_amount": limit,
                "spent_amount": spent,
                "remaining_amount": remaining,
                "percentage_used": pct,
                "status": status,
                "period": period
            })
        return results

    def set_budget(self, user_id: str, category: str, limit_amount: float, period: str = "2026-08") -> Dict[str, Any]:
        existing = self.repo.find(lambda b: b.get("user_id") == user_id and b.get("category") == category and b.get("period") == period)
        if existing:
            self.repo.update(existing[0]["id"], {"limit_amount": float(limit_amount)})
            return existing[0]
        else:
            new_b = {
                "id": f"bgt_{uuid.uuid4().hex[:12]}",
                "user_id": user_id,
                "category": category.upper(),
                "limit_amount": float(limit_amount),
                "period": period,
                "created_at": datetime.utcnow().isoformat()
            }
            self.repo.add(new_b)
            return new_b
