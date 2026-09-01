"""
Savings Goals Service
"""
import uuid
from datetime import datetime
from typing import List, Dict, Any
from storage.file_storage import FileStorageEngine
from storage.json_repository import JsonRepository

class SavingsService:
    def __init__(self, storage: FileStorageEngine):
        self.repo = JsonRepository(storage, "savings_goals.json", id_field="id")
        self._ensure_sample_goals()

    def _ensure_sample_goals(self):
        goals = self.repo.get_all()
        if not goals:
            sample_goals = [
                ("user_customer_01", "Emergency Reserve Fund", "EMERGENCY_FUND", 50000.00, 35000.00, "2026-12-31")
            ]
            for u_id, name, cat, target, curr, target_dt in sample_goals:
                g = {
                    "id": f"goal_{uuid.uuid4().hex[:12]}",
                    "user_id": u_id,
                    "goal_name": name,
                    "category": cat,
                    "target_amount": float(target),
                    "current_amount": float(curr),
                    "target_date": target_dt,
                    "monthly_contribution": round((target - curr) / 12, 2),
                    "created_at": datetime.utcnow().isoformat()
                }
                self.repo.add(g)

    def get_user_goals(self, user_id: str) -> List[Dict[str, Any]]:
        goals = self.repo.find(lambda g: g.get("user_id") == user_id)
        for g in goals:
            target = g.get("target_amount", 1.0)
            curr = g.get("current_amount", 0.0)
            g["progress_pct"] = min(round((curr / target) * 100, 1), 100.0) if target > 0 else 0.0
            g["remaining_amount"] = round(target - curr, 2)
        return goals

    def add_goal(self, user_id: str, goal_name: str, target_amount: float, target_date: str, monthly_contribution: float = 1000.0) -> Dict[str, Any]:
        new_g = {
            "id": f"goal_{uuid.uuid4().hex[:12]}",
            "user_id": user_id,
            "goal_name": goal_name,
            "category": "GENERAL",
            "target_amount": float(target_amount),
            "current_amount": 0.0,
            "target_date": target_date,
            "monthly_contribution": float(monthly_contribution),
            "created_at": datetime.utcnow().isoformat()
        }
        self.repo.add(new_g)
        return new_g

    def create_goal(self, user_id: str, goal_name: str, target_amount: float, target_date: str, monthly_contribution: float = 1000.0) -> Dict[str, Any]:
        return self.add_goal(user_id, goal_name, target_amount, target_date, monthly_contribution)

    def contribute(self, goal_id: str, amount: float) -> tuple[bool, str]:
        g = self.repo.get_by_id(goal_id)
        if not g:
            return False, "Goal not found."
        new_curr = round(g.get("current_amount", 0.0) + amount, 2)
        self.repo.update(goal_id, {"current_amount": new_curr})
        return True, f"Contributed ₹{amount:,.2f} to '{g.get('goal_name')}'."

    def add_contribution(self, goal_id: str, amount: float) -> tuple[bool, str]:
        return self.contribute(goal_id, amount)
