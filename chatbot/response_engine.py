"""
Master Chatbot Response Engine.
Unites NLP analysis, Knowledge Base retrieval, Policy execution, and Confidence scoring.
"""

import time
from config import Config
from nlp.intent_classifier import intent_classifier
from nlp.sentiment_analyzer import sentiment_analyzer
from nlp.entity_extractor import entity_extractor
from chatbot.confidence_scorer import confidence_scorer
from chatbot.policy_engine import policy_engine
from chatbot.context_manager import context_manager
from chatbot.fallback_handler import fallback_handler
from chatbot.escalation_manager import escalation_manager
from repositories.knowledge_repository import knowledge_repository
from repositories.message_repository import message_repository

class ResponseEngine:
    """Master Response Generator."""

    def process_message(self, conversation_id: str, user_message: str, user_id: str = None) -> dict:
        """Process incoming user message and generate intelligent response."""
        start_time = time.time()

        # 1. Store incoming user message
        user_msg_rec = message_repository.add_message(conversation_id, "user", user_message)

        # 2. NLP Pipeline: Intent, Sentiment, Entities
        intent_res = intent_classifier.classify(user_message)
        sentiment_res = sentiment_analyzer.analyze(user_message)
        entities = entity_extractor.extract_entities(user_message)

        # 3. Knowledge Base Lookup
        kb_articles = knowledge_repository.search_articles(user_message)
        kb_score = 0.9 if kb_articles else 0.0

        # 4. Compute Confidence Score
        confidence = confidence_scorer.calculate(
            intent_prob=intent_res["confidence"],
            sentiment_conf=sentiment_res["confidence"],
            has_entities=bool(entities),
            kb_score=kb_score
        )

        # 5. Evaluate Policy Engine
        policy = policy_engine.determine_action(
            intent=intent_res["intent"],
            confidence=confidence,
            sentiment=sentiment_res["sentiment"]
        )

        # 6. Generate Response Text
        if policy["action"] == "ESCALATE":
            escalation_manager.escalate_conversation(conversation_id, reason="Low confidence score")
            response_text = "I have flagged this request for human assistance. A support agent will review your conversation shortly."
            should_escalate = True
        elif kb_articles:
            best_article = kb_articles[0]
            response_text = f"According to our knowledge base article '{best_article['title']}':\n\n{best_article['content']}"
            should_escalate = False
        else:
            response_text = Config.INTENT_RESPONSES.get(
                intent_res["intent"],
                "Thank you for your message. How else may I assist you?"
            )
            should_escalate = False

        processing_ms = round((time.time() - start_time) * 1000, 2)

        # 7. Store Bot Response
        bot_metadata = {
            "intent": intent_res["intent"],
            "sentiment": sentiment_res["sentiment"],
            "confidence": confidence,
            "processing_time_ms": processing_ms,
            "escalated": should_escalate,
            "kb_article_id": kb_articles[0]["id"] if kb_articles else None
        }
        bot_msg_rec = message_repository.add_message(conversation_id, "bot", response_text, metadata=bot_metadata)

        # 8. Update Context State
        context_manager.update_context(conversation_id, intent_res["intent"], entities)

        return {
            "message": bot_msg_rec,
            "intent": intent_res["intent"],
            "sentiment": sentiment_res["sentiment"],
            "confidence": confidence,
            "processing_time_ms": processing_ms,
            "escalated": should_escalate,
            "entities": entities
        }

response_engine = ResponseEngine()
