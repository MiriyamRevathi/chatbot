"""
REST API User Feedback Endpoints.
"""

from flask import Blueprint, request, jsonify
from auth.rbac import login_required
from feedback.feedback_service import feedback_service

api_feedback_bp = Blueprint("api_feedback", __name__, url_prefix="/api/feedback")

@api_feedback_bp.route("", methods=["POST"])
@login_required
def submit_feedback():
    data = request.get_json() or {}
    fb = feedback_service.submit_feedback(
        message_id=data.get("message_id"),
        conversation_id=data.get("conversation_id"),
        is_helpful=data.get("is_helpful", True),
        comment=data.get("comment", "")
    )
    return jsonify({"status": "success", "feedback": fb})
