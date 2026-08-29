"""
Role-Based Access Control (RBAC) & Route Security Decorators.
"""

from functools import wraps
from flask import session, request, jsonify, redirect, url_for, flash
from config import Config
from core.exceptions import AuthorizationError, AuthenticationError
from repositories.user_repository import user_repository

# Permission Definitions
PERMISSIONS = {
    Config.ROLE_USER: ["chat:read", "chat:write", "knowledge:read", "feedback:write"],
    Config.ROLE_SUPPORT_AGENT: ["chat:read", "chat:write", "conversations:manage", "knowledge:read", "knowledge:write", "feedback:write"],
    Config.ROLE_ML_ENGINEER: ["chat:read", "chat:write", "nlp:lab", "models:manage", "experiments:manage", "knowledge:read"],
    Config.ROLE_ADMIN: ["chat:read", "chat:write", "conversations:manage", "knowledge:read", "knowledge:write", "nlp:lab", "models:manage", "experiments:manage", "admin:access", "diagnostics:view", "users:manage"]
}

def get_current_user():
    """Retrieve currently authenticated user record from session."""
    user_id = session.get("user_id")
    if not user_id:
        return None
    return user_repository.find_by_id(user_id)

def login_required(f):
    """Decorator requiring an active authenticated user session."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            if request.path.startswith("/api/"):
                return jsonify({"error": "Authentication required", "status_code": 401}), 401
            return redirect(url_for("auth.login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def role_required(*allowed_roles):
    """Decorator enforcing specific user roles."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if "user_id" not in session:
                if request.path.startswith("/api/"):
                    return jsonify({"error": "Authentication required", "status_code": 401}), 401
                return redirect(url_for("auth.login"))

            user_role = session.get("user_role", Config.ROLE_USER)
            if user_role not in allowed_roles and user_role != Config.ROLE_ADMIN:
                if request.path.startswith("/api/"):
                    return jsonify({"error": "Forbidden: Insufficient role permissions", "status_code": 403}), 403
                flash("Access denied: You do not have permission to view this resource.", "danger")
                return redirect(url_for("dashboard.index"))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def has_permission(role: str, permission: str) -> bool:
    """Check if a given role possesses a specific permission."""
    role_perms = PERMISSIONS.get(role, [])
    return permission in role_perms or role == Config.ROLE_ADMIN
