"""
Multi-Turn Dialogue Context & State Tracking.
"""

class ContextManager:
    """Tracks dialogue state and active intent slots."""

    def __init__(self):
        self._contexts = {}

    def get_context(self, conversation_id: str) -> dict:
        """Get current context dictionary for conversation."""
        return self._contexts.get(conversation_id, {
            "last_intent": None,
            "slots": {},
            "turns": 0
        })

    def update_context(self, conversation_id: str, intent: str, entities: list):
        """Update context with new turn details."""
        ctx = self.get_context(conversation_id)
        ctx["last_intent"] = intent
        ctx["turns"] = ctx.get("turns", 0) + 1
        for e in entities:
            ctx["slots"][e["type"]] = e["entity"]
        self._contexts[conversation_id] = ctx

context_manager = ContextManager()
