"""
Admin Dashboard Blueprint Routes
Handles user management, audit log viewing, and system diagnostics.
"""

from flask import Blueprint, render_template, session, current_app
from security.rbac import RBAC
from services.user_service import UserService
from storage.file_storage import FileStorageEngine

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/")
@RBAC.require_role(["ADMIN"])
def index():
    storage = FileStorageEngine(current_app.config["DATA_DIR"])
    user_service = UserService(storage)
    users = user_service.repo.get_all()
    return render_template("admin/index.html", users=users)
