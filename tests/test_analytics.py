"""
Tests for Analytics Aggregator.
"""

from analytics.aggregator import analytics_aggregator

def test_analytics_aggregator():
    metrics = analytics_aggregator.get_summary_metrics()
    assert "total_conversations" in metrics
    assert "average_confidence" in metrics
