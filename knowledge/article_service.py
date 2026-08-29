"""
High-Level Knowledge Article Management Service.
"""

from repositories.knowledge_repository import knowledge_repository
from core.validator import Validator
from core.exceptions import NotFoundError

class ArticleService:
    """Service managing Knowledge Base lifecycle."""

    def create_article(self, title: str, category: str, content: str, tags: list = None, author: str = "Admin") -> dict:
        """Validate and create article."""
        validated = Validator.validate_knowledge_article({
            "title": title, "category": category, "content": content, "tags": tags or []
        })
        return knowledge_repository.create_article(
            title=validated["title"],
            category=validated["category"],
            content=validated["content"],
            tags=validated["tags"],
            author=author
        )

    def get_article(self, article_id: str) -> dict:
        """Get article and increment view counter."""
        article = knowledge_repository.find_by_id(article_id)
        if not article:
            raise NotFoundError(f"Article {article_id} not found.")
        knowledge_repository.increment_view(article_id)
        return article

    def delete_article(self, article_id: str) -> bool:
        """Delete article by ID."""
        return knowledge_repository.delete(article_id)

article_service = ArticleService()
