"""
Budget Blueprint Routes
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from security.rbac import RBAC
from services.budget_service import BudgetService
from storage.file_storage import FileStorageEngine

budget_bp = Blueprint("budget", __name__, url_prefix="/budget")

def get_budget_service():
    storage = FileStorageEngine(current_app.config["DATA_DIR"])
    return BudgetService(storage)

@budget_bp.route("/")
@RBAC.require_auth
def index():
    user_id = session.get("user_id")
    service = get_budget_service()
    budgets = service.get_user_budgets_with_progress(user_id)
    total_budgeted = sum(b.get("limit_amount", 0) for b in budgets)
    total_spent = sum(b.get("spent_amount", 0) for b in budgets)
    overall_pct = round((total_spent / total_budgeted) * 100, 1) if total_budgeted > 0 else 0.0
    return render_template("budget/index.html", budgets=budgets, total_budgeted=total_budgeted, total_spent=total_spent, overall_pct=overall_pct)

@budget_bp.route("/set", methods=["POST"])
@RBAC.require_auth
def set_budget():
    user_id = session.get("user_id")
    category = request.form.get("category", "").strip()
    limit_amount = float(request.form.get("limit_amount", 0.0))
    if not category or limit_amount <= 0:
        flash("Valid category and limit amount required.", "danger")
        return redirect(url_for("budget.index"))
    service = get_budget_service()
    service.set_budget(user_id, category, limit_amount)
    flash(f"Monthly budget for '{category.upper()}' set to ₹{limit_amount:,.2f}.", "success")
    return redirect(url_for("budget.index"))

@budget_bp.route("/<b_id>/delete", methods=["POST"])
@RBAC.require_auth
def delete_budget(b_id):
    service = get_budget_service()
    service.repo.delete(b_id)
    flash("Budget deleted successfully!", "success")
    return redirect(url_for("budget.index"))
