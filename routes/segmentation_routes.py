"""
Customer Segmentation Blueprint Routes
"""
from flask import Blueprint, render_template, session, current_app
from security.rbac import RBAC
from ml.segmentation import CustomerSegmentation

segmentation_bp = Blueprint("segmentation", __name__, url_prefix="/segmentation")

@segmentation_bp.route("/")
@RBAC.require_role(["ANALYST", "ADMIN"])
def index():
    seg = CustomerSegmentation()
    sample_users = [
        [4500.0, 12000.0, 45800.0, 89350.0, 0.0],
        [8500.0, 7200.0, 5200.0, 1200.0, 3500.0],
        [3200.0, 1500.0, 25000.0, 150000.0, 0.0],
        [6000.0, 5800.0, 1200.0, 0.0, 15000.0],
        [2800.0, 2700.0, 800.0, 0.0, 28000.0]
    ]
    results = seg.segment_users(sample_users)
    return render_template("segmentation/index.html", results=results)
