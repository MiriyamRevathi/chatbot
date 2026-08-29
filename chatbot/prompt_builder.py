"""
Contextual Prompt Construction Engine.
"""

class PromptBuilder:
    """Prompt Builder for Dynamic Bot Responses."""

    @staticmethod
    def build_prompt(user_message: str, intent: str, entities: list, history: list) -> str:
        """Construct structured prompt context."""
        formatted_entities = ", ".join([f"{e['type']}:{e['entity']}" for e in entities]) if entities else "None"
        history_summary = "\n".join([f"{m['sender'].upper()}: {m['text']}" for m in history[-3:]]) if history else "No history"

        prompt = f"""
[USER INTENT]: {intent}
[DETECTED ENTITIES]: {formatted_entities}
[CONVERSATION HISTORY]:
{history_summary}
[CURRENT MESSAGE]: {user_message}
"""
        return prompt.strip()

prompt_builder = PromptBuilder()
