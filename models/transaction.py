"""
Transaction Domain Model
"""
from dataclasses import dataclass, asdict

@dataclass
class Transaction:
    id: str
    account_id: str
    user_id: str
    amount: float
    transaction_type: str  # INCOME, EXPENSE, TRANSFER
    category: str
    merchant: str
    transaction_date: str
    description: str = ""
    payment_method: str = "DEBIT_CARD"
    is_flagged_fraud: bool = False
    anomaly_score: float = 0.0
    created_at: str = ""

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})
