"""
Savings Goals Blueprint Routes
Handles savings goal lists, creation, and contribution deposits.
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
    total_target = sum(g["target_amount"] for g in goals)
    total_saved = sum(g["current_amount"] for g in goals)
    overall_pct = round((total_saved / total_target) * 100, 1) if total_target > 0 else 0.0
    return render_template("savings/index.html", goals=goals, total_target=total_target, total_saved=total_saved, overall_pct=overall_pct)

@savings_bp.route("/add", methods=["POST"])
@RBAC.require_auth
def add_goal():
    user_id = session.get("user_id")
    name = request.form.get("goal_name", "").strip()
    category = request.form.get("category", "CUSTOM")
    target = float(request.form.get("target_amount", 0.0))
    target_date = request.form.get("target_date")
    if not name or target <= 0:
        flash("Valid goal name and target amount required.", "danger")
        return redirect(url_for("savings.index"))
    service = get_savings_service()
    g = service.add_goal(user_id, name, category, target, target_date)
    flash(f"Savings goal '{g['goal_name']}' created successfully!", "success")
    return redirect(url_for("savings.index"))

@savings_bp.route("/contribute/<goal_id>", methods=["POST"])
@RBAC.require_auth
def contribute(goal_id):
    amount = float(request.form.get("amount", 0.0))
    if amount <= 0:
        flash("Contribution amount must be positive.", "danger")
        return redirect(url_for("savings.index"))
    service = get_savings_service()
    ok, msg = service.contribute(goal_id, amount)
    if ok:
        flash(msg, "success")
    else:
        flash(msg, "danger")
    return redirect(url_for("savings.index"))
