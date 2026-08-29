"""
REST API Model Playground Endpoints.
"""

from flask import Blueprint, request, jsonify
from auth.rbac import login_required, role_required
from models.trainer import model_trainer
from models.model_registry import model_registry
from repositories.model_repository import model_repository
from config import Config

api_models_bp = Blueprint("api_models", __name__, url_prefix="/api/models")

@api_models_bp.route("", methods=["GET"])
@login_required
def get_models():
    models = model_repository.get_all()
    return jsonify({"status": "success", "models": models})

@api_models_bp.route("/train", methods=["POST"])
@login_required
@role_required(Config.ROLE_ML_ENGINEER, Config.ROLE_ADMIN)
def train_model():
    data = request.get_json() or {}
    algo = data.get("algorithm", "naive_bayes")
    name = data.get("name", "Custom Model")
    res = model_trainer.train_intent_model(algorithm=algo, name=name)
    return jsonify({"status": "success", "model": res})
