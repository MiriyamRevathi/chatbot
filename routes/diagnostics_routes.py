"""
System Diagnostics View Blueprint.
"""

from flask import Blueprint, render_template
from auth.rbac import login_required, role_required, get_current_user
from monitoring.diagnostics_service import diagnostics_service
from config import Config

diagnostics_bp = Blueprint("diagnostics", __name__)

@diagnostics_bp.route("/diagnostics")
@login_required
def index():
    user = get_current_user()
    diag = diagnostics_service.get_diagnostics()
    return render_template("diagnostics.html", user=user, diag=diag)
