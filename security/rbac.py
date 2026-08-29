"""
Role-Based Access Control (RBAC) System
Defines permissions for Customer, Financial Analyst, and Administrator roles.
"""

from functools import wraps
from flask import session, redirect, url_for, flash, abort, jsonify, request

class RBAC:
    ROLES = {
        "CUSTOMER": 1,
        "ANALYST": 2,
        "ADMIN": 3
    }

    @classmethod
    def get_user_role(cls) -> str:
        return session.get("user_role", "CUSTOMER")

    @classmethod
    def is_authenticated(cls) -> bool:
        return "user_id" in session

    @classmethod
    def require_auth(cls, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not session.get("user_id"):
                if request.is_json:
                    return jsonify({"error": "Unauthorized"}), 401
                flash("Please log in to access this page.", "warning")
                return redirect(url_for("auth.login"))
            return f(*args, **kwargs)
        return decorated

    @classmethod
    def require_role(cls, required_roles: list[str]):
        def decorator(f):
            @wraps(f)
            def decorated(*args, **kwargs):
                if not session.get("user_id"):
                    flash("Please log in first.", "warning")
                    return redirect(url_for("auth.login"))
                current_role = session.get("user_role", "CUSTOMER")
                if current_role not in required_roles:
                    flash("You do not have permission to access this resource.", "danger")
                    return redirect(url_for("dashboard.index"))
                return f(*args, **kwargs)
            return decorated
        return decorator
