"""
Credit Scoring Blueprint Routes
Handles credit score display, factor analytics, and credit score improvement simulator.
"""

from flask import Blueprint, render_template, request, session, current_app
from security.rbac import RBAC
from services.credit_service import CreditService
from storage.file_storage import FileStorageEngine

credit_bp = Blueprint("credit", __name__, url_prefix="/credit")

def get_credit_service():
    storage = FileStorageEngine(current_app.config["DATA_DIR"])
    return CreditService(storage)

@credit_bp.route("/")
@RBAC.require_auth
def index():
    user_id = session.get("user_id")
    service = get_credit_service()
    profile = service.calculate_credit_score(user_id)
    return render_template("credit/index.html", profile=profile)
