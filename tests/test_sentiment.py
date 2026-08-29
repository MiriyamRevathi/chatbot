"""
Tests for Sentiment Analysis Engine.
"""

from nlp.sentiment_analyzer import sentiment_analyzer

def test_sentiment_analyzer_positive():
    res = sentiment_analyzer.analyze("Great service, fast response and helpful team!")
    assert res["sentiment"] == "positive"
    assert res["score"] > 0.0

def test_sentiment_analyzer_negative():
    res = sentiment_analyzer.analyze("Terrible experience, app crashed and support was useless.")
    assert res["sentiment"] == "negative"
    assert res["score"] < 0.0
