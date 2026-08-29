"""
Authentication UI View Blueprint.
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from auth.auth_service import auth_service
from auth.rbac import login_required, get_current_user
from core.exceptions import ChatFlowException

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        try:
            user = auth_service.login(email, password)
            flash(f"Welcome back, {user['name']}!", "success")
            return redirect(url_for("dashboard.index"))
        except ChatFlowException as e:
            flash(e.message, "danger")
    return render_template("auth/login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        role = request.form.get("role", "USER")
        try:
            user = auth_service.register(email, name, password, role)
            flash("Account registered successfully! Welcome to ChatFlow.", "success")
            return redirect(url_for("dashboard.index"))
        except ChatFlowException as e:
            flash(e.message, "danger")
    return render_template("auth/register.html")

@auth_bp.route("/logout")
def logout():
    auth_service.logout()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))
