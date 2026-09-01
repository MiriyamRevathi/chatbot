"""
Bank Account Management Service
"""
import uuid
import random
from datetime import datetime
from typing import List, Optional, Dict, Any
from storage.file_storage import FileStorageEngine
from storage.json_repository import JsonRepository
from models.account import Account

class AccountService:
    def __init__(self, storage: FileStorageEngine):
        self.repo = JsonRepository(storage, "accounts.json", id_field="id")
        self._ensure_demo_accounts()

    def _ensure_demo_accounts(self):
        accounts = self.repo.get_all()
        if not accounts:
            demo_accs = [
                Account(
                    id="acc_checking_01",
                    user_id="user_customer_01",
                    account_number="CHK-98421049",
                    account_name="Primary Checking Account",
                    account_type="CHECKING",
                    balance=12450.75,
                    currency="USD",
                    is_active=True,
                    created_at=datetime.utcnow().isoformat(),
                    interest_rate=0.05
                ),
                Account(
                    id="acc_savings_01",
                    user_id="user_customer_01",
                    account_number="SAV-88319204",
                    account_name="High Yield Savings",
                    account_type="SAVINGS",
                    balance=45800.00,
                    currency="USD",
                    is_active=True,
                    created_at=datetime.utcnow().isoformat(),
                    interest_rate=4.25
                )
            ]
            for a in demo_accs:
                self.repo.add(a.to_dict())

    def get_user_accounts(self, user_id: str) -> List[Account]:
        accs = self.repo.find(lambda a: a.get("user_id") == user_id and a.get("is_active", True))
        return [Account.from_dict(a) for a in accs]

    def get_account_by_id(self, account_id: str) -> Optional[Account]:
        data = self.repo.get_by_id(account_id)
        return Account.from_dict(data) if data else None

    def create_account(self, user_id: str, account_name: str, account_type: str, initial_balance: float, interest_rate: float = 0.0) -> Account:
        prefix = account_type[:3].upper()
        random_digits = "".join([str(random.randint(0, 9)) for _ in range(8)])
        new_acc = Account(
            id=f"acc_{uuid.uuid4().hex[:12]}",
            user_id=user_id,
            account_number=f"{prefix}-{random_digits}",
            account_name=account_name,
            account_type=account_type.upper(),
            balance=float(initial_balance),
            currency="USD",
            is_active=True,
            created_at=datetime.utcnow().isoformat(),
            interest_rate=float(interest_rate)
        )
        self.repo.add(new_acc.to_dict())
        return new_acc

    def add_account(self, user_id: str, account_name: str, account_type: str, initial_balance: float) -> Account:
        return self.create_account(user_id, account_name, account_type, initial_balance)

    def update_balance(self, account_id: str, amount_change: float) -> tuple[bool, str, float]:
        acc = self.get_account_by_id(account_id)
        if not acc:
            return False, "Account not found.", 0.0
        new_balance = round(acc.balance + amount_change, 2)
        self.repo.update(account_id, {"balance": new_balance})
        return True, "Balance updated.", new_balance

    def get_user_net_worth_summary(self, user_id: str) -> Dict[str, float]:
        accs = self.get_user_accounts(user_id)
        total_assets = sum(a.balance for a in accs if a.balance > 0)
        total_liabilities = sum(abs(a.balance) for a in accs if a.balance < 0)
        net_worth = total_assets - total_liabilities
        return {
            "total_assets": round(total_assets, 2),
            "total_liabilities": round(total_liabilities, 2),
            "net_worth": round(net_worth, 2),
            "checking_balance": round(sum(a.balance for a in accs if a.account_type == "CHECKING"), 2),
            "savings_balance": round(sum(a.balance for a in accs if a.account_type == "SAVINGS"), 2),
            "investment_balance": round(sum(a.balance for a in accs if a.account_type == "INVESTMENT"), 2)
        }
