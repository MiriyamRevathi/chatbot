"""
NLP Playground Lab View Blueprint.
"""

from flask import Blueprint, render_template
from auth.rbac import login_required, get_current_user

nlp_lab_bp = Blueprint("nlp_lab", __name__)

@nlp_lab_bp.route("/nlp-lab")
@login_required
def index():
    user = get_current_user()
    return render_template("nlp_lab.html", user=user)
