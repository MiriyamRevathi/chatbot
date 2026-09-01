"""
Account Blueprint Routes
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
    name = request.form.get("account_name", "").strip() or "New Checking Account"
    acc_type = request.form.get("account_type", "CHECKING")
    balance = float(request.form.get("balance", 0.0))
    
    service = get_account_service()
    service.add_account(user_id, name, acc_type, balance)
    flash(f"Account '{name}' added successfully!", "success")
    return redirect(url_for("accounts.index"))
