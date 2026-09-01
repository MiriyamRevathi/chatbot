"""
Savings Blueprint Routes
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from security.rbac import RBAC
from services.savings_service import SavingsService
from storage.file_storage import FileStorageEngine

savings_bp = Blueprint("savings", __name__, url_prefix="/savings")

def get_savings_service():
    storage = FileStorageEngine(current_app.config["DATA_DIR"])
    return SavingsService(storage)

@savings_bp.route("/")
@RBAC.require_auth
def index():
    user_id = session.get("user_id")
    service = get_savings_service()
    goals = service.get_user_goals(user_id)
    total_saved = sum(g.get("current_amount", 0) for g in goals)
    return render_template("savings/index.html", goals=goals, total_saved=total_saved)

@savings_bp.route("/add", methods=["POST"])
@RBAC.require_auth
def add_goal():
    user_id = session.get("user_id")
    name = request.form.get("goal_name", "").strip() or "New Savings Goal"
    target = float(request.form.get("target_amount", 10000.0))
    contrib = float(request.form.get("monthly_contribution", 1000.0))
    target_date = request.form.get("target_date", "2026-12-31")
    
    service = get_savings_service()
    service.create_goal(user_id, name, target, target_date, contrib)
    flash(f"Savings Goal '{name}' created!", "success")
    return redirect(url_for("savings.index"))

@savings_bp.route("/contribute", methods=["POST"])
@RBAC.require_auth
def add_contribution():
    goal_id = request.form.get("goal_id")
    amount = float(request.form.get("amount", 500.0))
    service = get_savings_service()
    service.add_contribution(goal_id, amount)
    flash(f"Contribution of ₹{amount:,.2f} added to goal!", "success")
    return redirect(url_for("savings.index"))
