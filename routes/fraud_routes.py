"""
Fraud Detection Blueprint Routes
Handles fraud monitoring dashboard, anomaly alert reviews, and ML system status.
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from security.rbac import RBAC
from ml.fraud_detection import MLFraudDetector
from services.transaction_service import TransactionService
from storage.file_storage import FileStorageEngine

fraud_bp = Blueprint("fraud", __name__, url_prefix="/fraud")

def get_services():
    storage = FileStorageEngine(current_app.config["DATA_DIR"])
    return TransactionService(storage), MLFraudDetector()

@fraud_bp.route("/")
@RBAC.require_role(["ANALYST", "ADMIN"])
def index():
    user_id = session.get("user_id")
    tx_service, ml_detector = get_services()
    all_txs = tx_service.get_user_transactions(user_id)

    # Convert dataclass transactions to dict for ML processing
    tx_dicts = [t.to_dict() for t in all_txs]
    evaluated_txs = ml_detector.train_and_predict(tx_dicts)

    fraud_alerts = [t for t in evaluated_txs if t.get("is_flagged_fraud")]
    high_risk_count = len([t for t in evaluated_txs if t.get("risk_level") == "HIGH"])

    return render_template(
        "fraud/index.html",
        transactions=evaluated_txs,
        fraud_alerts=fraud_alerts,
        high_risk_count=high_risk_count
    )
