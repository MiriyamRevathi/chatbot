"""
VADER-style Rule and Lexicon Sentiment Engine.
"""

POSITIVE_WORDS = set([
    "good", "great", "excellent", "amazing", "wonderful", "fantastic", "awesome",
    "love", "happy", "pleased", "delighted", "helpful", "thanks", "thank", "thankyou",
    "best", "perfect", "resolved", "brilliant", "superb", "top", "outstanding",
    "impressive", "fast", "friendly", "satisfied", "enjoy", "like", "positive"
])

NEGATIVE_WORDS = set([
    "bad", "terrible", "horrible", "awful", "poor", "unhappy", "dissatisfied",
    "broken", "error", "bug", "crash", "worst", "hate", "useless", "disappointed",
    "slow", "charge", "refund", "complaint", "fail", "failed", "failing", "unacceptable",
    "annoyed", "frustrated", "angry", "negative", "crap", "rubbish"
])

class LexiconSentiment:
    """Lexicon and Rule Based Sentiment Engine."""

    @staticmethod
    def analyze(tokens: list) -> dict:
        """Compute lexicon polarity score and sentiment label."""
        pos_count = sum(1 for t in tokens if t.lower() in POSITIVE_WORDS)
        neg_count = sum(1 for t in tokens if t.lower() in NEGATIVE_WORDS)

        total = pos_count + neg_count
        if total == 0:
            return {"sentiment": "neutral", "score": 0.0, "confidence": 0.8}

        score = (pos_count - neg_count) / total

        if score > 0.15:
            sentiment = "positive"
        elif score < -0.15:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        confidence = round(min(1.0, 0.6 + 0.1 * total), 4)
        return {"sentiment": sentiment, "score": round(score, 4), "confidence": confidence}

lexicon_sentiment = LexiconSentiment()
