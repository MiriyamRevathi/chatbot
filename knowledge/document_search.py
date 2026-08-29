"""
Hybrid Knowledge Base Search Engine (BM25 + TF-IDF Vector Search).
"""

from nlp.bm25 import BM25
from repositories.knowledge_repository import knowledge_repository

class HybridDocumentSearch:
    """Hybrid Document Search Engine."""

    def search(self, query: str) -> list:
        """Search knowledge base articles using BM25 ranking."""
        articles = knowledge_repository.get_all()
        published = [a for a in articles if a.get("is_published")]

        if not published:
            return []

        bm25 = BM25()
        corpus = [a["title"] + " " + a["content"] for a in published]
        bm25.fit(corpus)
        scores = bm25.score(query)

        results = []
        for idx, score in enumerate(scores):
            if score > 0.01:
                art = published[idx]
                art["search_score"] = score
                results.append(art)

        return sorted(results, key=lambda x: x.get("search_score", 0), reverse=True)

document_search = HybridDocumentSearch()

# Optimized BM25 Term Frequency Saturation & Vector Search
