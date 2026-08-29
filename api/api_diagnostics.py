"""
REST API Health and System Diagnostics Endpoints.
"""

from flask import Blueprint, jsonify
from monitoring.diagnostics_service import diagnostics_service
from monitoring.health_checker import health_checker

api_diag_bp = Blueprint("api_diagnostics", __name__, url_prefix="/api")

@api_diag_bp.route("/health", methods=["GET"])
def health():
    h = health_checker.get_system_health()
    return jsonify(h)

@api_diag_bp.route("/diagnostics", methods=["GET"])
def diagnostics():
    d = diagnostics_service.get_diagnostics()
    return jsonify(d)
