"""
Okapi BM25 Document Ranking Algorithm Implementation.
"""

import math
from collections import Counter
from nlp.tokenizer import Tokenizer

class BM25:
    """Okapi BM25 Scoring Model."""

    def __init__(self, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.doc_len = []
        self.avg_doc_len = 0.0
        self.doc_freqs = []
        self.idf = {}
        self.doc_tokens = []

    def fit(self, corpus: list):
        """Fit BM25 parameters on corpus of document strings."""
        self.doc_tokens = [Tokenizer.tokenize_words(d) for d in corpus]
        N = len(corpus)

        self.doc_len = [len(d) for d in self.doc_tokens]
        self.avg_doc_len = sum(self.doc_len) / N if N > 0 else 1.0

        df = Counter()
        for doc in self.doc_tokens:
            for term in set(doc):
                df[term] += 1

        for term, freq in df.items():
            self.idf[term] = math.log((N - freq + 0.5) / (freq + 0.5) + 1.0)

        return self

    def score(self, query: str) -> list:
        """Score all documents against search query."""
        q_tokens = Tokenizer.tokenize_words(query)
        scores = []

        for idx, doc in enumerate(self.doc_tokens):
            score = 0.0
            doc_len = self.doc_len[idx]
            freqs = Counter(doc)

            for term in q_tokens:
                if term not in freqs:
                    continue
                tf = freqs[term]
                idf = self.idf.get(term, 0.0)
                num = tf * (self.k1 + 1)
                denom = tf + self.k1 * (1 - self.b + self.b * (doc_len / self.avg_doc_len))
                score += idf * (num / denom)

            scores.append(round(score, 4))
        return scores
