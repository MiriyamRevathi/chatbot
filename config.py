"""
FinTechHub Configuration Module
Handles application configuration, paths, feature flags, and environment settings.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
REPORTS_DIR = BASE_DIR / "reports" / "generated"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "fintechhub_secure_local_development_secret_key_2026")
    DATA_DIR = DATA_DIR
    REPORTS_DIR = REPORTS_DIR
    SESSION_TYPE = "filesystem"
    PERMANENT_SESSION_LIFETIME = 86400
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    
    USERS_FILE = DATA_DIR / "users.json"
    ACCOUNTS_FILE = DATA_DIR / "accounts.json"
    TRANSACTIONS_FILE = DATA_DIR / "transactions.json"
    BUDGETS_FILE = DATA_DIR / "budgets.json"
    SAVINGS_FILE = DATA_DIR / "savings_goals.json"
    HOLDINGS_FILE = DATA_DIR / "holdings.json"
    LOANS_FILE = DATA_DIR / "loans.json"
    CREDIT_FILE = DATA_DIR / "credit_profiles.json"
    FRAUD_ALERTS_FILE = DATA_DIR / "fraud_alerts.json"
    AUDIT_LOGS_FILE = DATA_DIR / "audit_logs.json"
    NOTIFICATIONS_FILE = DATA_DIR / "notifications.json"
    
    ENABLE_ML_FRAUD_DETECTION = True
    ENABLE_FORECASTING = True
    ENABLE_CUSTOMER_SEGMENTATION = True
    ENABLE_PDF_REPORTS = True
    
    ROLES = {
        "CUSTOMER": "Customer",
        "ANALYST": "Financial Analyst",
        "ADMIN": "Administrator"
    }

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig,
    "default": DevelopmentConfig
}
# PR 1 feature commit

# Feature PR 01: feature/core-infrastructure-storage

# Feature PR 02: feature/user-authentication-rbac

# Feature PR 03: feature/financial-math-accounts

# Feature PR 04: feature/transaction-management-processor

# Feature PR 05: feature/budget-planning-analytics

# Feature PR 06: feature/savings-goals-planner

# Feature PR 07: feature/investment-portfolio-system

# Feature PR 08: feature/loan-amortization-emi

# Feature PR 09: feature/credit-scoring-simulation

# Feature PR 10: feature/ml-fraud-detection-pipeline

# Feature PR 11: feature/spending-forecasting-segmentation
