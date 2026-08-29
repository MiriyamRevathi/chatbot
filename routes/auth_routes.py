"""
Authentication Blueprint Routes
Handles register, login, logout, profile view, password change, and user settings.
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from security.rbac import RBAC
from services.user_service import UserService
from storage.file_storage import FileStorageEngine

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

def get_user_service():
    storage = FileStorageEngine(current_app.config["DATA_DIR"])
    return UserService(storage)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if session.get("user_id"):
        return redirect(url_for("dashboard.index"))
    if request.method == "POST":
        username_or_email = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        service = get_user_service()
        user = service.authenticate(username_or_email, password)
        if user:
            session.clear()
            session["user_id"] = user.id
            session["username"] = user.username
            session["user_role"] = user.role
            session["full_name"] = user.full_name
            flash(f"Welcome back, {user.full_name}!", "success")
            return redirect(url_for("dashboard.index"))
        else:
            flash("Invalid credentials or deactivated account.", "danger")
    return render_template("auth/login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if session.get("user_id"):
        return redirect(url_for("dashboard.index"))
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        full_name = request.form.get("full_name", "").strip()
        role = request.form.get("role", "CUSTOMER")
        service = get_user_service()
        user, msg = service.register_user(username, email, password, full_name, role)
        if user:
            flash(f"Registration successful! Please log in.", "success")
            return redirect(url_for("auth.login"))
        else:
            flash(msg, "danger")
    return render_template("auth/register.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))

@auth_bp.route("/profile", methods=["GET", "POST"])
@RBAC.require_auth
def profile():
    service = get_user_service()
    user_id = session.get("user_id")
    user = service.get_by_id(user_id)
    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip()
        ok, msg = service.update_profile(user_id, full_name, phone, email)
        if ok:
            session["full_name"] = full_name
            flash(msg, "success")
            user = service.get_by_id(user_id)
        else:
            flash(msg, "danger")
    return render_template("auth/profile.html", user=user)

@auth_bp.route("/change-password", methods=["POST"])
@RBAC.require_auth
def change_password():
    service = get_user_service()
    user_id = session.get("user_id")
    old_pw = request.form.get("old_password", "")
    new_pw = request.form.get("new_password", "")
    ok, msg = service.change_password(user_id, old_pw, new_pw)
    if ok:
        flash(msg, "success")
    else:
        flash(msg, "danger")
    return redirect(url_for("auth.profile"))
