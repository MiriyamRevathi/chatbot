"""
Dashboard Blueprint Routes
Renders Customer, Financial Analyst, and Admin dashboards with analytics widgets.
"""

from flask import Blueprint, render_template, session, current_app, redirect, url_for
from security.rbac import RBAC
from services.account_service import AccountService
from services.transaction_service import TransactionService
from analytics.risk_engine import FinancialRiskEngine
from storage.file_storage import FileStorageEngine

dashboard_bp = Blueprint("dashboard", __name__)

def get_services():
    storage = FileStorageEngine(current_app.config["DATA_DIR"])
    return AccountService(storage), TransactionService(storage)

@dashboard_bp.route("/")
@RBAC.require_auth
def index():
    user_id = session.get("user_id")
    role = session.get("user_role", "CUSTOMER")
    
    acc_service, tx_service = get_services()
    summary = acc_service.get_user_net_worth_summary(user_id)
    recent_txs = tx_service.get_user_transactions(user_id)[:5]
    category_summary = tx_service.get_category_breakdown(user_id)
    
    risk_metrics = FinancialRiskEngine.calculate_health_and_risk(
        monthly_income=3450.00,
        monthly_expenses=1950.00,
        total_assets=summary["total_assets"],
        total_liabilities=summary["total_liabilities"],
        credit_score=760
    )

    if role == "ADMIN":
        return render_template("dashboard/admin.html", summary=summary, risk_metrics=risk_metrics)
    elif role == "ANALYST":
        return render_template("dashboard/analyst.html", summary=summary, risk_metrics=risk_metrics)
    else:
        return render_template(
            "dashboard/customer.html",
            summary=summary,
            recent_transactions=recent_txs,
            category_summary=category_summary,
            risk_metrics=risk_metrics
        )
