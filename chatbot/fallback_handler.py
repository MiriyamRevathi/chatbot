"""
Intelligent Fallback and Clarification Handler.
"""

FALLBACK_RESPONSES = [
    "I'm not completely sure I understood that. Could you rephrase your question?",
    "I want to make sure I give you the right answer. Could you provide a bit more detail?",
    "I'm having trouble matching your request to a specific help article. Would you like to speak to a human support agent?"
]

class FallbackHandler:
    """Fallback Response Handler."""

    @staticmethod
    def get_fallback_response(intent_info: dict) -> dict:
        """Construct fallback response with suggestions."""
        return {
            "response": FALLBACK_RESPONSES[0],
            "suggestions": ["View Billing FAQ", "Reset Password", "Speak to Support Agent"],
            "is_fallback": True
        }

fallback_handler = FallbackHandler()
