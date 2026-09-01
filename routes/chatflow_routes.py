"""
ChatFlow Blueprint Routes
Provides the /chatflow web page and API endpoint for conversational financial assistance.
"""

from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for, current_app
from security.rbac import RBAC
from services.chatflow_service import ChatFlowService
from services.account_service import AccountService
from services.transaction_service import TransactionService
from services.budget_service import BudgetService
from services.savings_service import SavingsService
from services.investment_service import InvestmentService
from services.loan_service import LoanService
from services.credit_service import CreditService
from storage.file_storage import FileStorageEngine

chatflow_bp = Blueprint("chatflow", __name__, url_prefix="/chatflow")

def get_chatflow_service():
    storage = FileStorageEngine(current_app.config["DATA_DIR"])
    acc_svc = AccountService(storage)
    txn_svc = TransactionService(storage)
    bgt_svc = BudgetService(storage)
    svg_svc = SavingsService(storage)
    inv_svc = InvestmentService(storage)
    lon_svc = LoanService(storage)
    crd_svc = CreditService(storage)
    return ChatFlowService(acc_svc, txn_svc, bgt_svc, svg_svc, inv_svc, lon_svc, crd_svc)

@chatflow_bp.route("", methods=["GET"])
@RBAC.require_auth
def index():
    user_id = session.get("user_id")
    history = session.get("chatflow_history", [])
    return render_template("chatflow/index.html", history=history)

@chatflow_bp.route("/query", methods=["POST"])
@RBAC.require_auth
def query():
    user_id = session.get("user_id")
    data = request.get_json() or {}
    message_text = data.get("message", "").strip()
    if not message_text:
        return jsonify({"error": "Message text cannot be empty."}), 400

    service = get_chatflow_service()
    response_data = service.process_query(user_id, message_text)

    # Save to session history
    history = session.get("chatflow_history", [])
    history.append({"sender": "user", "text": message_text})
    history.append({
        "sender": "assistant",
        "text": response_data.get("text"),
        "cards": response_data.get("cards", []),
        "breakdown": response_data.get("breakdown", []),
        "actions": response_data.get("actions", [])
    })
    session["chatflow_history"] = history[-20:] # Keep last 20 messages

    return jsonify(response_data)

@chatflow_bp.route("/clear", methods=["POST"])
@RBAC.require_auth
def clear_history():
    session["chatflow_history"] = []
    return jsonify({"status": "success", "message": "Conversation history cleared."})
