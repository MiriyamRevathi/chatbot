"""
REST API Experiment Tracking Endpoints.
"""

from flask import Blueprint, request, jsonify
from auth.rbac import login_required
from experiments.experiment_service import experiment_service

api_exp_bp = Blueprint("api_experiments", __name__, url_prefix="/api/experiments")

@api_exp_bp.route("", methods=["GET"])
@login_required
def get_experiments():
    exps = experiment_service.list_experiments()
    return jsonify({"status": "success", "experiments": exps})
