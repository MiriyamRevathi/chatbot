"""
Knowledge Base Category Taxonomy Service.
"""

KNOWLEDGE_CATEGORIES = [
    "Billing", "Account", "Technical", "Products", "Orders", "Security", "Subscriptions", "General"
]

class CategoryService:
    """Category Taxonomy Manager."""

    @staticmethod
    def get_all_categories() -> list:
        """Return list of valid knowledge categories."""
        return KNOWLEDGE_CATEGORIES

category_service = CategoryService()
