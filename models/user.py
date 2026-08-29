"""
User Domain Model
"""
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class User:
    id: str
    username: str
    email: str
    password_hash: str
    role: str = "CUSTOMER"
    full_name: str = ""
    phone: str = ""
    is_active: bool = True
    created_at: str = ""
    updated_at: str = ""

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})
