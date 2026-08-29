"""
Investment Blueprint Routes
Handles portfolio summary, holdings management, asset allocation, and simulated market updates.
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
    portfolio = service.get_user_portfolio(user_id)
    return render_template("investments/index.html", portfolio=portfolio)

@investment_bp.route("/add", methods=["POST"])
@RBAC.require_auth
def add_holding():
    user_id = session.get("user_id")
    symbol = request.form.get("symbol", "").strip()
    name = request.form.get("name", "").strip()
    asset_cls = request.form.get("asset_class", "STOCKS")
    qty = float(request.form.get("quantity", 0.0))
    buy_px = float(request.form.get("purchase_price", 0.0))
    curr_px = float(request.form.get("current_price", buy_px))
    
    if not symbol or qty <= 0 or buy_px <= 0:
        flash("Valid symbol, quantity, and purchase price required.", "danger")
        return redirect(url_for("investments.index"))
        
    service = get_investment_service()
    service.add_holding(user_id, symbol, name or symbol, asset_cls, qty, buy_px, curr_px)
    flash(f"Holding '{symbol.upper()}' added to portfolio!", "success")
    return redirect(url_for("investments.index"))

@investment_bp.route("/simulate-tick", methods=["POST"])
@RBAC.require_auth
def simulate_tick():
    user_id = session.get("user_id")
    service = get_investment_service()
    service.simulate_market_tick(user_id)
    flash("Simulated live market price fluctuations!", "info")
    return redirect(url_for("investments.index"))
