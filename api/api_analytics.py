"""
REST API Analytics Endpoints.
"""

from flask import Blueprint, jsonify
from auth.rbac import login_required
from analytics.analytics_service import analytics_service

api_analytics_bp = Blueprint("api_analytics", __name__, url_prefix="/api/analytics")

@api_analytics_bp.route("", methods=["GET"])
@login_required
def get_analytics():
    stats = analytics_service.get_dashboard_stats()
    return jsonify({"status": "success", "analytics": stats})
