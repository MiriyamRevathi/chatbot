"""
Loan Blueprint Routes
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
    total_debt = sum(l.get("principal_amount", 0) for l in loans) or 245000.0
    return render_template("loans/index.html", loans=loans, total_debt=total_debt)

@loan_bp.route("/add", methods=["POST"])
@RBAC.require_auth
def add_loan():
    user_id = session.get("user_id")
    name = request.form.get("loan_name", "").strip() or "Personal Loan"
    principal = float(request.form.get("principal_amount", 100000.0))
    rate = float(request.form.get("interest_rate", 10.5))
    tenure = int(request.form.get("tenure_months", 36))
    
    service = get_loan_service()
    service.add_loan(user_id, name, principal, rate, tenure)
    flash(f"Loan '{name}' added successfully!", "success")
    return redirect(url_for("loans.index"))

@loan_bp.route("/<loan_id>/delete", methods=["POST"])
@RBAC.require_auth
def delete_loan(loan_id):
    service = get_loan_service()
    service.repo.delete(loan_id)
    flash("Loan account deleted!", "success")
    return redirect(url_for("loans.index"))

@loan_bp.route("/calculator")
@RBAC.require_auth
def calculator():
    return render_template("loans/calculator.html")
