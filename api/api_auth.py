"""
REST API Authentication Endpoints.
"""

from flask import Blueprint, request, jsonify
from auth.auth_service import auth_service
from auth.rbac import get_current_user, login_required
from core.exceptions import ChatFlowException

api_auth_bp = Blueprint("api_auth", __name__, url_prefix="/api/auth")

@api_auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    try:
        user = auth_service.login(data.get("email"), data.get("password"))
        return jsonify({"status": "success", "user": user})
    except ChatFlowException as e:
        return jsonify(e.to_dict()), e.status_code

@api_auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    try:
        user = auth_service.register(data.get("email"), data.get("name"), data.get("password"), data.get("role", "USER"))
        return jsonify({"status": "success", "user": user})
    except ChatFlowException as e:
        return jsonify(e.to_dict()), e.status_code

@api_auth_bp.route("/me", methods=["GET"])
@login_required
def me():
    user = get_current_user()
    return jsonify({"status": "success", "user": user})
