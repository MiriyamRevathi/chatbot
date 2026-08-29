"""
Tests for Intent Classification & Preprocessing.
"""

from nlp.intent_classifier import intent_classifier
from nlp.preprocessor import preprocessor

def test_text_preprocessor():
    raw = "<h1>Hello WORLD! 123</h1>"
    cleaned = preprocessor.clean(raw)
    assert "hello world" in cleaned

def test_intent_classification():
    res = intent_classifier.classify("i want a refund for my order")
    assert res["intent"] in ["refund", "billing", "order_status", "help"]
    assert res["confidence"] > 0.0
