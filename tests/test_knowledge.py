"""
Tests for Knowledge Base Search & Retrieval.
"""

from repositories.knowledge_repository import knowledge_repository
from knowledge.document_search import document_search

def test_knowledge_search():
    results = knowledge_repository.search_articles("invoice")
    assert isinstance(results, list)
    assert len(results) > 0

def test_bm25_document_search():
    results = document_search.search("password reset")
    assert isinstance(results, list)
