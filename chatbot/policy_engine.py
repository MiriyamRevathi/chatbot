"""
Intent-to-Action Policy Routing Engine.
"""

from config import Config

class PolicyEngine:
    """Policy Engine evaluating conversation rules."""

    @staticmethod
    def determine_action(intent: str, confidence: float, sentiment: str) -> dict:
        """Evaluate business policy and determine bot action."""
        if confidence < Config.HUMAN_ESCALATION_THRESHOLD:
            return {
                "action": "ESCALATE",
                "reason": "Confidence below threshold",
                "requires_human": True
            }

        if sentiment == "negative" and intent in ["complaint", "billing", "refund"]:
            return {
                "action": "PRIORITY_RESPONSE",
                "reason": "Negative sentiment detected on sensitive intent",
                "requires_human": False
            }

        return {
            "action": "NORMAL_RESPONSE",
            "reason": "High confidence intent match",
            "requires_human": False
        }

policy_engine = PolicyEngine()
