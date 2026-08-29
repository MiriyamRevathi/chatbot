"""
Admin Panel View Blueprint.
"""

from flask import Blueprint, render_template
from auth.rbac import login_required, role_required, get_current_user
from repositories.user_repository import user_repository
from repositories.audit_repository import audit_repository
from config import Config

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin")
@login_required
@role_required(Config.ROLE_ADMIN)
def index():
    user = get_current_user()
    users = user_repository.get_all()
    audit_logs = audit_repository.get_all()
    return render_template("admin.html", user=user, users=users, audit_logs=audit_logs)
