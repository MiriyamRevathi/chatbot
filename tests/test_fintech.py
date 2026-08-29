import pytest
import os
from pathlib import Path
from storage.file_storage import FileStorageEngine
from services.user_service import UserService
from services.account_service import AccountService
from services.transaction_service import TransactionService
from services.budget_service import BudgetService
from services.savings_service import SavingsService
from services.investment_service import InvestmentService
from services.loan_service import LoanService
from services.credit_service import CreditService
from finance.tvm_engine import TVMEngine
from finance.financial_ratios import FinancialRatioEngine
from finance.tax_calculator import TaxCalculatorEngine
from ml.fraud_detection import MLFraudDetector
from ml.forecasting import SpendingForecaster
from ml.segmentation import CustomerSegmentation
from analytics.risk_engine import FinancialRiskEngine

@pytest.fixture
def temp_storage(tmp_path):
    return FileStorageEngine(tmp_path)

def test_user_service_registration_and_auth(temp_storage):
    service = UserService(temp_storage)
    user, msg = service.register_user("testuser", "test@fintech.local", "SecurePass123!", "Test User", "CUSTOMER")
    assert user is not None
    assert user.username == "testuser"
    
    auth_user = service.authenticate("testuser", "SecurePass123!")
    assert auth_user is not None
    assert auth_user.id == user.id

def test_tvm_engine_calculations():
    fv = TVMEngine.future_value(0.05, 10, 0, -10000)
    assert round(fv, 2) == 16288.95
    cagr = TVMEngine.cagr(10000, 16288.95, 10)
    assert round(cagr, 4) == 0.05

def test_financial_ratios():
    ratios = FinancialRatioEngine.evaluate_full_ratio_profile({
        "total_assets": 50000,
        "total_liabilities": 10000,
        "monthly_income": 6000,
        "monthly_expenses": 3500
    })
    assert ratios["current_ratio"] == 5.0
    assert ratios["savings_ratio"] == 41.67

def test_tax_calculator():
    tax_data = TaxCalculatorEngine.calculate_federal_tax(85000.0)
    assert tax_data["taxable_income"] == 70400.0
    assert tax_data["total_federal_tax"] > 0

def test_ml_fraud_detection():
    detector = MLFraudDetector()
    txs = [
        {"amount": 15.0, "category": "DINING", "transaction_date": "2026-08-01"},
        {"amount": 45.0, "category": "GROCERIES", "transaction_date": "2026-08-02"},
        {"amount": 12.0, "category": "ENTERTAINMENT", "transaction_date": "2026-08-03"},
        {"amount": 89.0, "category": "TRANSPORTATION", "transaction_date": "2026-08-04"},
        {"amount": 9500.0, "category": "MISCELLANEOUS", "transaction_date": "2026-08-05"}
    ]
    res = detector.train_and_predict(txs)
    assert len(res) == 5
    flagged = [t for t in res if t["is_flagged_fraud"]]
    assert len(flagged) >= 1

def test_spending_forecaster():
    historical = [1200.0, 1300.0, 1400.0, 1500.0]
    preds = SpendingForecaster.forecast_next_months(historical, 3)
    assert len(preds) == 3
    assert preds[0] > 1500.0

def test_customer_segmentation():
    seg = CustomerSegmentation(n_clusters=3)
    user_features = [
        [5000.0, 10000.0, 50000.0, 100000.0, 0.0],
        [2000.0, 1800.0, 500.0, 0.0, 5000.0],
        [8000.0, 4000.0, 20000.0, 300000.0, 0.0]
    ]
    clusters = seg.segment_users(user_features)
    assert len(clusters) == 3

def test_financial_risk_engine():
    risk = FinancialRiskEngine.calculate_health_and_risk(
        monthly_income=5000.0,
        monthly_expenses=2500.0,
        total_assets=40000.0,
        total_liabilities=5000.0,
        credit_score=750
    )
    assert risk["financial_health_score"] > 60.0
    assert risk["risk_level"] in ["LOW", "MODERATE", "HIGH"]
