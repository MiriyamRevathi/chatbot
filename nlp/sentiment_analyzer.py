"""
Unified Hybrid Sentiment Analyzer.
Combines Lexicon and Machine Learning engines for robust sentiment classification.
"""

from nlp.tokenizer import Tokenizer
from nlp.lexicon_sentiment import lexicon_sentiment
from nlp.ml_sentiment import ml_sentiment

class SentimentAnalyzer:
    """Hybrid Sentiment Analyzer."""

    def analyze(self, text: str) -> dict:
        """Analyze text and return sentiment label, score, confidence, and emotion breakdown."""
        if not text:
            return {"sentiment": "neutral", "score": 0.0, "confidence": 1.0, "emotions": {"joy": 0, "anger": 0}}

        tokens = Tokenizer.tokenize_words(text)
        lex_res = lexicon_sentiment.analyze(tokens)
        ml_res = ml_sentiment.predict(text)

        # Ensembled Sentiment
        combined_score = round(0.5 * lex_res["score"] + 0.5 * ml_res["score"], 4)
        if combined_score > 0.1:
            final_sentiment = "positive"
        elif combined_score < -0.1:
            final_sentiment = "negative"
        else:
            final_sentiment = "neutral"

        confidence = round((lex_res["confidence"] + ml_res["confidence"]) / 2.0, 4)

        # Basic Emotion Estimation
        emotions = {
            "joy": 0.8 if final_sentiment == "positive" else 0.1,
            "anger": 0.8 if final_sentiment == "negative" else 0.1,
            "neutrality": 0.8 if final_sentiment == "neutral" else 0.2
        }

        return {
            "sentiment": final_sentiment,
            "score": combined_score,
            "confidence": confidence,
            "emotions": emotions
        }

sentiment_analyzer = SentimentAnalyzer()
