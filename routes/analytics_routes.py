"""
Analytics Dashboard View Blueprint.
"""

from flask import Blueprint, render_template
from auth.rbac import login_required, get_current_user
from analytics.analytics_service import analytics_service

analytics_bp = Blueprint("analytics", __name__)

@analytics_bp.route("/analytics")
@login_required
def index():
    user = get_current_user()
    stats = analytics_service.get_dashboard_stats()
    return render_template("analytics.html", user=user, stats=stats)
