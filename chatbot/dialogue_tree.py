"""
Structured Dialogue Tree Engine.
Executes multi-step decision tree flows for guided support troubleshooting.
"""

class DialogueTreeEngine:
    """Executes structured dialogue flows."""

    def execute_flow(self, flow_name: str, step: int) -> dict:
        """Execute step in a structured dialogue tree."""
        flows = {
            "password_reset": [
                {"step": 1, "message": "Have you tried clicking 'Forgot Password' on the login page?", "options": ["Yes", "No"]},
                {"step": 2, "message": "Did you receive the password reset token in your email?", "options": ["Yes", "No"]},
                {"step": 3, "message": "Great! Please follow the link in your email to choose a new password.", "options": ["Finished"]}
            ]
        }
        steps = flows.get(flow_name, [])
        if step <= len(steps):
            return steps[step - 1]
        return {"step": step, "message": "Flow completed.", "options": []}

dialogue_tree = DialogueTreeEngine()
