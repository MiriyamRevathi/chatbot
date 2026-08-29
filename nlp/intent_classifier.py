"""
Master Intent Classifier Engine integrating ML Models and Datasets.
"""

from config import Config
from nlp.tfidf import TFIDFVectorizer
from nlp.naive_bayes import MultinomialNaiveBayes
from nlp.logistic_regression import LogisticRegressionOVR
from nlp.preprocessor import TextPreprocessor

class IntentClassifier:
    """Master Intent Classifier for ChatFlow Platform."""

    def __init__(self, model_type="naive_bayes"):
        self.model_type = model_type
        self.vectorizer = TFIDFVectorizer()
        self.preprocessor = TextPreprocessor()
        self.model = None
        self.is_trained = False
        self.train_on_default_corpus()

    def train_on_default_corpus(self):
        """Train classifier using default Intent Dataset in Config."""
        documents = []
        labels = []

        for intent, phrases in Config.INTENT_DATASET.items():
            for p in phrases:
                documents.append(p)
                labels.append(intent)

        # Fit TF-IDF Vectorizer
        X_vectors = self.vectorizer.fit_transform(documents)

        # Instantiate Model
        if self.model_type == "logistic_regression":
            self.model = LogisticRegressionOVR(lr=0.5, max_iter=50)
            self.model.fit(X_vectors, labels)
        else:
            self.model = MultinomialNaiveBayes(alpha=1.0)
            self.model.fit(X_vectors, labels, self.vectorizer.get_feature_names())

        self.is_trained = True

    def classify(self, text: str) -> dict:
        """Classify intent for raw input text and return probabilities."""
        if not text or not self.is_trained:
            return {"intent": "greeting", "confidence": 0.5, "probabilities": {}}

        clean_text = self.preprocessor.clean(text)
        vec = self.vectorizer.transform([clean_text])
        probas = self.model.predict_proba(vec)[0]

        top_intent = max(probas, key=probas.get)
        confidence = probas[top_intent]

        # Apply fallback if low confidence
        if confidence < 0.2:
            top_intent = "help"
            confidence = 0.4

        return {
            "intent": top_intent,
            "confidence": round(confidence, 4),
            "probabilities": probas
        }

intent_classifier = IntentClassifier()
