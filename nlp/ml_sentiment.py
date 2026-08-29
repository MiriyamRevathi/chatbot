"""
Machine Learning Sentiment Analysis Classifier.
"""

from nlp.tfidf import TFIDFVectorizer
from nlp.naive_bayes import MultinomialNaiveBayes

class MLSentimentClassifier:
    """TF-IDF Naive Bayes ML Sentiment Model."""

    def __init__(self):
        self.vectorizer = TFIDFVectorizer()
        self.model = MultinomialNaiveBayes()
        self._train_baseline()

    def _train_baseline(self):
        training_data = [
            ("Great application, very helpful and fast!", "positive"),
            ("Awesome support team, thank you so much!", "positive"),
            ("I love this product, works perfectly.", "positive"),
            ("Excellent service and easy to use interface.", "positive"),
            ("Standard service, normal experience.", "neutral"),
            ("Can you tell me how to check order status?", "neutral"),
            ("I need to update my password.", "neutral"),
            ("Where can I find billing invoices?", "neutral"),
            ("Terrible experience, app crashed three times!", "negative"),
            ("I want a refund, worst service ever.", "negative"),
            ("Horrible customer support and slow response.", "negative"),
            ("Broken feature, 500 server error again.", "negative")
        ]

        docs = [d[0] for d in training_data]
        labels = [d[1] for d in training_data]

        X_vecs = self.vectorizer.fit_transform(docs)
        self.model.fit(X_vecs, labels, self.vectorizer.get_feature_names())

    def predict(self, text: str) -> dict:
        """Predict sentiment label and probabilities."""
        vec = self.vectorizer.transform([text])
        probas = self.model.predict_proba(vec)[0]
        top_sentiment = max(probas, key=probas.get)
        score = probas.get("positive", 0.0) - probas.get("negative", 0.0)

        return {
            "sentiment": top_sentiment,
            "score": round(score, 4),
            "confidence": round(probas[top_sentiment], 4)
        }

ml_sentiment = MLSentimentClassifier()
