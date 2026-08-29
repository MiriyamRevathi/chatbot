"""
Request Validation and Data Schema Utilities.
"""

from core.exceptions import ValidationError
from core.security import is_valid_email

class Validator:
    """Request Payload Validation Helper."""

    @staticmethod
    def validate_registration(data: dict):
        """Validate registration request."""
        errors = {}
        email = data.get("email", "").strip()
        name = data.get("name", "").strip()
        password = data.get("password", "").strip()
        role = data.get("role", "USER").strip()

        if not email or not is_valid_email(email):
            errors["email"] = "Valid email address is required."
        if not name or len(name) < 2:
            errors["name"] = "Name must be at least 2 characters long."
        if not password or len(password) < 6:
            errors["password"] = "Password must be at least 6 characters long."

        if errors:
            raise ValidationError("Registration validation failed", errors=errors)
        return {"email": email, "name": name, "password": password, "role": role}

    @staticmethod
    def validate_chat_message(data: dict):
        """Validate chat message payload."""
        message = data.get("message", "").strip()
        if not message:
            raise ValidationError("Message content cannot be empty", errors={"message": "Required"})
        if len(message) > 4000:
            raise ValidationError("Message exceeds maximum length of 4000 characters", errors={"message": "Too long"})
        return message

    @staticmethod
    def validate_knowledge_article(data: dict):
        """Validate knowledge base article creation."""
        errors = {}
        title = data.get("title", "").strip()
        category = data.get("category", "").strip()
        content = data.get("content", "").strip()

        if not title:
            errors["title"] = "Title is required"
        if not category:
            errors["category"] = "Category is required"
        if not content or len(content) < 10:
            errors["content"] = "Content must be at least 10 characters long"

        if errors:
            raise ValidationError("Article validation failed", errors=errors)
        return {"title": title, "category": category, "content": content, "tags": data.get("tags", [])}
