"""
Transaction Management Service
"""
import uuid
from datetime import datetime
from typing import List, Dict, Any, Optional
from storage.file_storage import FileStorageEngine
from storage.json_repository import JsonRepository
from models.transaction import Transaction
from services.categorization_engine import CategorizationEngine

class TransactionService:
    def __init__(self, storage: FileStorageEngine):
        self.repo = JsonRepository(storage, "transactions.json", id_field="id")
        self._ensure_sample_transactions()

    def _ensure_sample_transactions(self):
        txs = self.repo.get_all()
        if not txs:
            sample_data = [
                ("acc_checking_01", "user_customer_01", 3450.00, "INCOME", "INCOME", "TechCorp Inc Payroll", "2026-08-01", "Monthly Salary Deposit", "DIRECT_DEPOSIT"),
                ("acc_checking_01", "user_customer_01", -145.20, "EXPENSE", "GROCERIES", "Whole Foods Market", "2026-08-03", "Weekly Organic Groceries", "DEBIT_CARD"),
                ("acc_checking_01", "user_customer_01", -12.50, "EXPENSE", "DINING", "Starbucks Coffee", "2026-08-04", "Morning Latte", "DEBIT_CARD")
            ]
            for acc_id, u_id, amt, t_type, cat, merch, dt, desc, p_meth in sample_data:
                tx = Transaction(
                    id=f"tx_{uuid.uuid4().hex[:12]}",
                    account_id=acc_id,
                    user_id=u_id,
                    amount=float(amt),
                    transaction_type=t_type,
                    category=cat,
                    merchant=merch,
                    transaction_date=dt,
                    description=desc,
                    payment_method=p_meth,
                    is_flagged_fraud=False,
                    anomaly_score=0.01,
                    created_at=datetime.utcnow().isoformat()
                )
                self.repo.add(tx.to_dict())

    def get_user_transactions(self, user_id: str, category: str = None, account_id: str = None, search: str = None) -> List[Transaction]:
        all_tx = [Transaction.from_dict(d) for d in self.repo.find(lambda t: t.get("user_id") == user_id)]
        if category:
            all_tx = [t for t in all_tx if t.category.upper() == category.upper()]
        if account_id:
            all_tx = [t for t in all_tx if t.account_id == account_id]
        if search:
            s = search.lower()
            all_tx = [t for t in all_tx if s in t.merchant.lower() or s in t.description.lower() or s in t.category.lower()]
        all_tx.sort(key=lambda t: t.transaction_date, reverse=True)
        return all_tx

    def add_transaction(self, user_id: str, account_id: str, amount: float, merchant: str, category: str = "", transaction_date: str = "", description: str = "", payment_method: str = "DEBIT_CARD") -> Transaction:
        if not category or category == "AUTO":
            category = CategorizationEngine.categorize(merchant, description, amount)
        t_type = "INCOME" if amount > 0 else "EXPENSE"
        new_tx = Transaction(
            id=f"tx_{uuid.uuid4().hex[:12]}",
            account_id=account_id,
            user_id=user_id,
            amount=float(amount),
            transaction_type=t_type,
            category=category.upper(),
            merchant=merchant,
            transaction_date=transaction_date or datetime.utcnow().strftime("%Y-%m-%d"),
            description=description,
            payment_method=payment_method,
            is_flagged_fraud=False,
            anomaly_score=0.0,
            created_at=datetime.utcnow().isoformat()
        )
        self.repo.add(new_tx.to_dict())
        return new_tx

    def delete_transaction(self, tx_id: str) -> bool:
        return self.repo.delete(tx_id)

    def get_category_breakdown(self, user_id: str) -> Dict[str, float]:
        txs = self.get_user_transactions(user_id)
        breakdown = {}
        for t in txs:
            if t.amount < 0:
                cat = t.category
                breakdown[cat] = round(breakdown.get(cat, 0.0) + abs(t.amount), 2)
        return breakdown
