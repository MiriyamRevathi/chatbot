"""
Account Management Blueprint Routes
Handles listing user accounts, adding new simulated bank/asset accounts, and viewing account details.
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from security.rbac import RBAC
from services.account_service import AccountService
from storage.file_storage import FileStorageEngine

account_bp = Blueprint("accounts", __name__, url_prefix="/accounts")

def get_account_service():
    storage = FileStorageEngine(current_app.config["DATA_DIR"])
    return AccountService(storage)

@account_bp.route("/")
@RBAC.require_auth
def index():
    user_id = session.get("user_id")
    service = get_account_service()
    accounts = service.get_user_accounts(user_id)
    summary = service.get_user_net_worth_summary(user_id)
    return render_template("accounts/index.html", accounts=accounts, summary=summary)

@account_bp.route("/add", methods=["POST"])
@RBAC.require_auth
def add_account():
    user_id = session.get("user_id")
    name = request.form.get("account_name", "").strip()
    acc_type = request.form.get("account_type", "CHECKING")
    balance = float(request.form.get("initial_balance", 0.0))
    rate = float(request.form.get("interest_rate", 0.0))
    
    if not name:
        flash("Account name is required.", "danger")
        return redirect(url_for("accounts.index"))
        
    service = get_account_service()
    acc = service.create_account(user_id, name, acc_type, balance, rate)
    flash(f"Account '{acc.account_name}' ({acc.account_number}) created successfully!", "success")
    return redirect(url_for("accounts.index"))
