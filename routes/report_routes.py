"""
Reports Blueprint Routes
Handles downloadable PDF & CSV financial statement reports.
"""

from flask import Blueprint, render_template, send_file, session, current_app, Response
from security.rbac import RBAC
from reports.pdf_generator import PDFReportGenerator
from services.account_service import AccountService
from services.transaction_service import TransactionService
from storage.file_storage import FileStorageEngine

report_bp = Blueprint("reports", __name__, url_prefix="/reports")

def get_services():
    storage = FileStorageEngine(current_app.config["DATA_DIR"])
    return AccountService(storage), TransactionService(storage)

@report_bp.route("/")
@RBAC.require_auth
def index():
    return render_template("reports/index.html")

@report_bp.route("/download/pdf")
@RBAC.require_auth
def download_pdf():
    user_id = session.get("user_id")
    user_name = session.get("full_name", "Customer")
    acc_service, _ = get_services()
    summary = acc_service.get_user_net_worth_summary(user_id)
    
    output_pdf = current_app.config["REPORTS_DIR"] / f"statement_{user_id}.pdf"
    PDFReportGenerator.generate_monthly_statement(output_pdf, user_name, summary, [])
    
    return send_file(str(output_pdf), as_attachment=True, download_name="FinTechHub_Statement.pdf")

@report_bp.route("/download/csv")
@RBAC.require_auth
def download_csv():
    user_id = session.get("user_id")
    _, tx_service = get_services()
    txs = tx_service.get_user_transactions(user_id)
    
    csv_data = "Date,Merchant,Category,Amount,Status\n"
    for tx in txs:
        tdate = getattr(tx, 'transaction_date', '2026-08-31') if hasattr(tx, 'transaction_date') else tx.get('transaction_date', '2026-08-31')
        tmerch = getattr(tx, 'merchant', 'Merchant') if hasattr(tx, 'merchant') else tx.get('merchant', 'Merchant')
        tcat = getattr(tx, 'category', 'General') if hasattr(tx, 'category') else tx.get('category', 'General')
        tamt = getattr(tx, 'amount', 0) if hasattr(tx, 'amount') else tx.get('amount', 0)
        csv_data += f"{tdate},{tmerch},{tcat},{tamt},Completed\n"
        
    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=FinTechHub_Statement.csv"}
    )
