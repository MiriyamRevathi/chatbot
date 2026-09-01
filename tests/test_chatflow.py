"""
Unit Tests for ChatFlow Service and Intent Engine
"""

import pytest
from app import create_app
from services.chatflow_service import ChatFlowService
from services.account_service import AccountService
from services.transaction_service import TransactionService
from services.budget_service import BudgetService
from services.savings_service import SavingsService
from services.investment_service import InvestmentService
from services.loan_service import LoanService
from services.credit_service import CreditService
from storage.file_storage import FileStorageEngine

@pytest.fixture
def client():
    app = create_app("dev")
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_chatflow_service_intents(tmp_path):
    storage = FileStorageEngine(tmp_path)
    svc = ChatFlowService(
        AccountService(storage),
        TransactionService(storage),
        BudgetService(storage),
        SavingsService(storage),
        InvestmentService(storage),
        LoanService(storage),
        CreditService(storage)
    )

    # Test Account Intent
    res1 = svc.process_query("test_user", "How much money do I have?")
    assert res1["intent"] == "ACCOUNT_SUMMARY"
    assert "cards" in res1

    # Test Spending Category Intent
    res2 = svc.process_query("test_user", "How much did I spend on food?")
    assert res2["intent"] in ["TRANSACTION_SUMMARY", "TRANSACTION_CATEGORY_ANALYSIS"]

    # Test Budget Intent
    res3 = svc.process_query("test_user", "Am I over my budget?")
    assert res3["intent"] == "BUDGET_STATUS"

    # Test EMI Calculation Intent
    res4 = svc.process_query("test_user", "Calculate EMI for 15000")
    assert res4["intent"] == "EMI_CALCULATION"
