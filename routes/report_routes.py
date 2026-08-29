"""
Reports Blueprint Routes
Handles downloadable PDF & CSV financial statement reports.
"""

from flask import Blueprint, render_template, send_file, session, current_app
from security.rbac import RBAC
from reports.pdf_generator import PDFReportGenerator
from services.account_service import AccountService
from storage.file_storage import FileStorageEngine
from pathlib import Path

report_bp = Blueprint("reports", __name__, url_prefix="/reports")

@report_bp.route("/")
@RBAC.require_auth
def index():
    return render_template("reports/index.html")

@report_bp.route("/download/pdf")
@RBAC.require_auth
def download_pdf():
    user_id = session.get("user_id")
    user_name = session.get("full_name", "Customer")
    storage = FileStorageEngine(current_app.config["DATA_DIR"])
    acc_service = AccountService(storage)
    summary = acc_service.get_user_net_worth_summary(user_id)
    
    output_pdf = current_app.config["REPORTS_DIR"] / f"statement_{user_id}.pdf"
    PDFReportGenerator.generate_monthly_statement(output_pdf, user_name, summary, [])
    
    return send_file(str(output_pdf), as_attachment=True, download_name=f"FinTechHub_Statement.pdf")
