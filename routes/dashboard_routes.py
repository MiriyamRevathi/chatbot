"""
Dashboard UI View Blueprint.
"""

from flask import Blueprint, render_template, session
from auth.rbac import login_required, get_current_user
from analytics.analytics_service import analytics_service
from repositories.conversation_repository import conversation_repository
from repositories.knowledge_repository import knowledge_repository

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
@dashboard_bp.route("/dashboard")
@login_required
def index():
    user = get_current_user()
    stats = analytics_service.get_dashboard_stats()
    user_convs = conversation_repository.get_user_conversations(user["id"])
    kb_count = len(knowledge_repository.get_all())
    return render_template("dashboard.html", user=user, stats=stats, recent_convs=user_convs[:5], kb_count=kb_count)
