"""
Tests for Chatbot Response Engine & Confidence Scorer.
"""

from chatbot.confidence_scorer import confidence_scorer
from chatbot.response_engine import response_engine
from repositories.conversation_repository import conversation_repository

def test_confidence_scorer():
    score = confidence_scorer.calculate(intent_prob=0.9, sentiment_conf=0.8, has_entities=True, kb_score=0.9)
    assert 0.0 <= score <= 1.0
    assert score > 0.8

def test_response_engine():
    conv = conversation_repository.create_conversation("user-1", "Test Chat")
    res = response_engine.process_message(conv["id"], "Hello, I need help with billing.")
    assert "intent" in res
    assert res["intent"] in ["greeting", "billing", "help"]
