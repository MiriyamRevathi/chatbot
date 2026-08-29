"""
Bank & Asset Account Domain Model
"""
from dataclasses import dataclass, asdict

@dataclass
class Account:
    id: str
    user_id: str
    account_number: str
    account_name: str
    account_type: str  # CHECKING, SAVINGS, CREDIT, INVESTMENT
    balance: float
    currency: str = "USD"
    is_active: bool = True
    created_at: str = ""
    interest_rate: float = 0.0

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})
