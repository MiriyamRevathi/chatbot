"""
Knowledge Base UI View Blueprint.
"""

from flask import Blueprint, render_template, request
from auth.rbac import login_required, get_current_user
from repositories.knowledge_repository import knowledge_repository
from knowledge.category_service import category_service

knowledge_bp = Blueprint("knowledge", __name__)

@knowledge_bp.route("/knowledge")
@login_required
def index():
    user = get_current_user()
    category = request.args.get("category")
    query = request.args.get("q", "")

    if query:
        articles = knowledge_repository.search_articles(query, category)
    elif category:
        articles = [a for a in knowledge_repository.get_all() if a.get("category", "").lower() == category.lower()]
    else:
        articles = knowledge_repository.get_all()

    categories = category_service.get_all_categories()
    return render_template("knowledge.html", user=user, articles=articles, categories=categories, current_cat=category, query=query)
