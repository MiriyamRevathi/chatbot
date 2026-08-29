"""
Knowledge Repository managing Articles and Documentation.
"""

from repositories.base_repository import BaseRepository
from datetime import datetime
import uuid

class KnowledgeRepository(BaseRepository):
    """Knowledge Base Repository."""

    def __init__(self):
        super().__init__("knowledge_articles.json")
        self.init_sample_articles()

    def init_sample_articles(self):
        """Seed initial knowledge articles."""
        if not self._read_all():
            samples = [
                {
                    "title": "Understanding Your Monthly Invoice & Billing Charges",
                    "category": "Billing",
                    "content": "Your monthly invoice contains detailed line items for base subscriptions, API usage, and add-on modules. Invoices are generated on the 1st of each month. If you see a discrepancy, contact support immediately.",
                    "tags": ["billing", "invoice", "payment", "charges"]
                },
                {
                    "title": "How to Reset Your Account Password",
                    "category": "Account",
                    "content": "To reset your password, click the 'Forgot Password' link on the login page. An email with a secure single-use token will be sent to your registered email address.",
                    "tags": ["password", "reset", "security", "account"]
                },
                {
                    "title": "Troubleshooting 500 Internal Server Errors in ChatFlow",
                    "category": "Technical",
                    "content": "A 500 Internal Error typically indicates an unhandled exception or storage read issue. Check system diagnostics at /diagnostics and verify local JSON file permissions.",
                    "tags": ["error", "500", "technical", "diagnostics"]
                },
                {
                    "title": "Upgrading and Managing Subscription Plans",
                    "category": "Subscriptions",
                    "content": "ChatFlow offers Free, Pro ($29/mo), and Enterprise tiers. You can upgrade or downgrade your plan at any time from the Subscription settings tab.",
                    "tags": ["subscription", "pricing", "plans", "upgrade"]
                },
                {
                    "title": "Requesting Refunds & Policy Terms",
                    "category": "Billing",
                    "content": "Refund requests are evaluated under our 14-day money-back guarantee policy. Submit a ticket under Billing > Refund to initiate processing.",
                    "tags": ["refund", "policy", "guarantee", "returns"]
                }
            ]
            for s in samples:
                self.create_article(s["title"], s["category"], s["content"], s["tags"])

    def create_article(self, title: str, category: str, content: str, tags: list = None, author: str = "Admin") -> dict:
        """Create a new knowledge base article."""
        article = {
            "id": str(uuid.uuid4()),
            "title": title.strip(),
            "category": category.strip(),
            "content": content.strip(),
            "tags": tags or [],
            "author": author,
            "is_published": True,
            "views": 0,
            "upvotes": 0,
            "downvotes": 0,
            "created_at": datetime.utcnow().isoformat() + "Z",
            "updated_at": datetime.utcnow().isoformat() + "Z"
        }
        return self.save(article)

    def search_articles(self, query: str, category: str = None) -> list:
        """Search articles by title, content, or tags."""
        records = self._read_all()
        q = query.lower()
        results = []
        for a in records:
            if not a.get("is_published"):
                continue
            if category and a.get("category").lower() != category.lower():
                continue
            title_match = q in a.get("title", "").lower()
            content_match = q in a.get("content", "").lower()
            tag_match = any(q in t.lower() for t in a.get("tags", []))
            if title_match or content_match or tag_match:
                results.append(a)
        return results

    def increment_view(self, article_id: str):
        """Record a view on an article."""
        article = self.find_by_id(article_id)
        if article:
            article["views"] = article.get("views", 0) + 1
            self.save(article)

knowledge_repository = KnowledgeRepository()
