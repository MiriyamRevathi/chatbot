"""
Model Playground View Blueprint.
"""

from flask import Blueprint, render_template
from auth.rbac import login_required, role_required, get_current_user
from repositories.model_repository import model_repository
from repositories.experiment_repository import experiment_repository
from config import Config

model_playground_bp = Blueprint("model_playground", __name__)

@model_playground_bp.route("/model-playground")
@login_required
@role_required(Config.ROLE_ML_ENGINEER, Config.ROLE_ADMIN)
def index():
    user = get_current_user()
    models = model_repository.get_all()
    experiments = experiment_repository.get_all()
    return render_template("model_playground.html", user=user, models=models, experiments=experiments)
