"""
Transaction Management Blueprint Routes
Handles transaction listing, adding, filtering, CSV export, and deletion.
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app, Response
from security.rbac import RBAC
from services.transaction_service import TransactionService
from services.account_service import AccountService
from storage.file_storage import FileStorageEngine

transaction_bp = Blueprint("transactions", __name__, url_prefix="/transactions")

def get_services():
    storage = FileStorageEngine(current_app.config["DATA_DIR"])
    return TransactionService(storage), AccountService(storage)

@transaction_bp.route("/")
@RBAC.require_auth
def index():
    user_id = session.get("user_id")
    category = request.args.get("category", "")
    account_id = request.args.get("account_id", "")
    search = request.args.get("search", "")
    
    tx_service, acc_service = get_services()
    transactions = tx_service.get_user_transactions(user_id, category, account_id, search)
    accounts = acc_service.get_user_accounts(user_id)
    category_summary = tx_service.get_category_breakdown(user_id)
    
    return render_template(
        "transactions/index.html",
        transactions=transactions,
        accounts=accounts,
        category_summary=category_summary,
        selected_category=category,
        selected_account=account_id,
        search_query=search
    )

@transaction_bp.route("/add", methods=["POST"])
@RBAC.require_auth
def add_transaction():
    user_id = session.get("user_id")
    account_id = request.form.get("account_id", "acc_default")
    amount = float(request.form.get("amount", 0.0))
    merchant = request.form.get("merchant", "").strip() or "General Transaction"
    category = request.form.get("category", "Food")
    tx_date = request.form.get("transaction_date") or "2026-08-31"
    desc = request.form.get("description", "").strip()
    pay_meth = request.form.get("payment_method", "DEBIT_CARD")
    
    tx_service, acc_service = get_services()
    tx = tx_service.add_transaction(user_id, account_id, amount, merchant, category, tx_date, desc, pay_meth)
    acc_service.update_balance(account_id, amount)
    
    flash(f"Transaction of ₹{abs(amount):,.2f} at '{merchant}' saved successfully!", "success")
    return redirect(url_for("transactions.index"))

@transaction_bp.route("/export", methods=["GET"])
@RBAC.require_auth
def export_csv():
    user_id = session.get("user_id")
    tx_service, _ = get_services()
    transactions = tx_service.get_user_transactions(user_id)
    
    csv_data = "Date,Merchant,Category,Account,Amount,Status\n"
    for tx in transactions:
        csv_data += f"{tx.get('transaction_date','')},{tx.get('merchant','')},{tx.get('category','')},{tx.get('account_id','')},{tx.get('amount',0)},Completed\n"
    
    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=fintechhub_transactions.csv"}
    )
