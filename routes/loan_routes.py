"""
Loan Blueprint Routes
Handles loan summaries, interactive EMI calculator, and amortization schedules.
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from security.rbac import RBAC
from services.loan_service import LoanService
from storage.file_storage import FileStorageEngine

loan_bp = Blueprint("loans", __name__, url_prefix="/loans")

def get_loan_service():
    storage = FileStorageEngine(current_app.config["DATA_DIR"])
    return LoanService(storage)

@loan_bp.route("/")
@RBAC.require_auth
def index():
    user_id = session.get("user_id")
    service = get_loan_service()
    loans = service.get_user_loans(user_id)
    total_principal = sum(l["principal_amount"] for l in loans)
    total_remaining = sum(l["remaining_balance"] for l in loans)
    total_emi = sum(l["monthly_emi"] for l in loans)
    return render_template("loans/index.html", loans=loans, total_principal=total_principal, total_remaining=total_remaining, total_emi=total_emi)

@loan_bp.route("/calculator", methods=["GET", "POST"])
def calculator():
    principal = float(request.form.get("principal", 250000.0))
    rate = float(request.form.get("interest_rate", 6.5))
    tenure = int(request.form.get("tenure_months", 360))
    service = get_loan_service()
    result = service.calculate_emi_details(principal, rate, tenure)
    return render_template("loans/calculator.html", result=result)
