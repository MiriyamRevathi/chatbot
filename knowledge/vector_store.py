"""
Local Vector Store for Knowledge Document Embeddings.
"""

from nlp.tfidf import TFIDFVectorizer
from nlp.cosine_similarity import cosine_similarity

class LocalVectorStore:
    """In-Memory Local Vector Index for Documents."""

    def __init__(self):
        self.vectorizer = TFIDFVectorizer()
        self.doc_ids = []
        self.vectors = []

    def index_documents(self, documents: list):
        """Index list of document dicts with 'id' and 'content'."""
        self.doc_ids = [d["id"] for d in documents]
        contents = [d["content"] for d in documents]
        if contents:
            self.vectors = self.vectorizer.fit_transform(contents)

    def search(self, query: str, top_k: int = 3) -> list:
        """Search top K document IDs by vector cosine similarity."""
        if not self.vectors:
            return []
        q_vec = self.vectorizer.transform([query])[0]
        scores = []
        for doc_id, doc_vec in zip(self.doc_ids, self.vectors):
            score = cosine_similarity.compute(q_vec, doc_vec)
            scores.append((doc_id, score))

        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
        return sorted_scores[:top_k]

local_vector_store = LocalVectorStore()
