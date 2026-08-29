"""
Custom TF-IDF Vectorizer from Scratch.
"""

import math
from collections import Counter
from nlp.tokenizer import Tokenizer
from nlp.preprocessor import TextPreprocessor

class TFIDFVectorizer:
    """TF-IDF Vectorizer with fit, transform, and fit_transform API."""

    def __init__(self, norm=True, sublinear_tf=True):
        self.norm = norm
        self.sublinear_tf = sublinear_tf
        self.vocabulary_ = {}
        self.idf_ = {}
        self.feature_names_ = []
        self.preprocessor = TextPreprocessor()

    def fit(self, raw_documents: list):
        """Build vocabulary and compute IDF for documents."""
        df = Counter()
        N = len(raw_documents)
        vocab = set()

        doc_tokens_list = []
        for doc in raw_documents:
            tokens = Tokenizer.tokenize_words(self.preprocessor.clean(doc))
            doc_tokens_list.append(tokens)
            unique_terms = set(tokens)
            vocab.update(unique_terms)
            for term in unique_terms:
                df[term] += 1

        self.feature_names_ = sorted(list(vocab))
        self.vocabulary_ = {term: i for i, term in enumerate(self.feature_names_)}

        # Compute smooth IDF: log((1 + N) / (1 + df)) + 1
        for term in self.feature_names_:
            self.idf_[term] = math.log((1 + N) / (1 + df[term])) + 1.0

        return self

    def transform(self, raw_documents: list) -> list:
        """Transform raw documents into TF-IDF feature vectors."""
        vectors = []
        for doc in raw_documents:
            tokens = Tokenizer.tokenize_words(self.preprocessor.clean(doc))
            tf = Counter(tokens)
            vec = [0.0] * len(self.feature_names_)

            for term, count in tf.items():
                if term in self.vocabulary_:
                    idx = self.vocabulary_[term]
                    term_tf = (1 + math.log(count)) if self.sublinear_tf else count
                    vec[idx] = term_tf * self.idf_[term]

            # L2 Normalization
            if self.norm:
                sq_sum = sum(x * x for x in vec)
                if sq_sum > 0:
                    norm_val = math.sqrt(sq_sum)
                    vec = [x / norm_val for x in vec]

            vectors.append(vec)
        return vectors

    def fit_transform(self, raw_documents: list) -> list:
        """Fit vocabulary and transform documents in one step."""
        return self.fit(raw_documents).transform(raw_documents)

    def get_feature_names(self) -> list:
        """Get ordered list of feature terms."""
        return self.feature_names_
