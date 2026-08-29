"""
REST API NLP Engine Endpoints (/api/nlp/analyze, /api/nlp/intent, etc.).
"""

from flask import Blueprint, request, jsonify
from auth.rbac import login_required
from nlp.preprocessor import preprocessor
from nlp.tokenizer import tokenizer
from nlp.intent_classifier import intent_classifier
from nlp.sentiment_analyzer import sentiment_analyzer
from nlp.entity_extractor import entity_extractor
from nlp.text_stats import text_stats
from nlp.similarity import text_similarity
from nlp.keyword_extractor import keyword_extractor

api_nlp_bp = Blueprint("api_nlp", __name__, url_prefix="/api/nlp")

@api_nlp_bp.route("/analyze", methods=["POST"])
@login_required
def analyze():
    data = request.get_json() or {}
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "Text payload is required"}), 422

    clean_text = preprocessor.clean(text)
    tokens = tokenizer.tokenize_words(text)
    intent_res = intent_classifier.classify(text)
    sentiment_res = sentiment_analyzer.analyze(text)
    entities = entity_extractor.extract_entities(text)
    stats = text_stats.analyze(text)
    keywords = keyword_extractor.extract_keywords(text)

    return jsonify({
        "status": "success",
        "original_text": text,
        "cleaned_text": clean_text,
        "tokens": tokens,
        "intent": intent_res,
        "sentiment": sentiment_res,
        "entities": entities,
        "statistics": stats,
        "keywords": keywords
    })

@api_nlp_bp.route("/intent", methods=["POST"])
@login_required
def intent():
    data = request.get_json() or {}
    text = data.get("text", "")
    res = intent_classifier.classify(text)
    return jsonify({"status": "success", "result": res})

@api_nlp_bp.route("/sentiment", methods=["POST"])
@login_required
def sentiment():
    data = request.get_json() or {}
    text = data.get("text", "")
    res = sentiment_analyzer.analyze(text)
    return jsonify({"status": "success", "result": res})
