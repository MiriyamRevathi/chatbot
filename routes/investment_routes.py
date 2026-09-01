"""
Investment Blueprint Routes
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from security.rbac import RBAC
from services.investment_service import InvestmentService
from storage.file_storage import FileStorageEngine

investment_bp = Blueprint("investments", __name__, url_prefix="/investments")

def get_investment_service():
    storage = FileStorageEngine(current_app.config["DATA_DIR"])
    return InvestmentService(storage)

@investment_bp.route("/")
@RBAC.require_auth
def index():
    user_id = session.get("user_id")
    service = get_investment_service()
    portfolio = service.get_portfolio_summary(user_id)
    return render_template("investments/index.html", portfolio=portfolio)

@investment_bp.route("/add", methods=["POST"])
@RBAC.require_auth
def add_investment():
    user_id = session.get("user_id")
    name = request.form.get("asset_name", "").strip() or "Index ETF Fund"
    category = request.form.get("asset_category", "EQUITY")
    amount = float(request.form.get("amount", 10000.0))
    buy_price = float(request.form.get("buy_price", 100.0))
    
    service = get_investment_service()
    service.add_investment(user_id, name, category, amount, buy_price)
    flash(f"Investment '{name}' recorded successfully!", "success")
    return redirect(url_for("investments.index"))
