"""
REST API Knowledge Base Endpoints.
"""

from flask import Blueprint, request, jsonify
from auth.rbac import login_required
from knowledge.article_service import article_service
from repositories.knowledge_repository import knowledge_repository

api_kb_bp = Blueprint("api_knowledge", __name__, url_prefix="/api/knowledge")

@api_kb_bp.route("", methods=["GET", "POST"])
@login_required
def knowledge_index():
    if request.method == "POST":
        data = request.get_json() or {}
        article = article_service.create_article(
            title=data.get("title"), category=data.get("category"), content=data.get("content"), tags=data.get("tags")
        )
        return jsonify({"status": "success", "article": article})

    query = request.args.get("q", "")
    category = request.args.get("category")
    if query:
        articles = knowledge_repository.search_articles(query, category)
    else:
        articles = knowledge_repository.get_all()

    return jsonify({"status": "success", "articles": articles})
