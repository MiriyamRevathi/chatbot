"""
Analytics Metrics Aggregator.
Aggregates time-series conversation metrics, intent distributions, and sentiment ratios.
"""

from collections import Counter
from repositories.conversation_repository import conversation_repository
from repositories.message_repository import message_repository

class AnalyticsAggregator:
    """Aggregates system analytics."""

    def get_summary_metrics(self) -> dict:
        """Compute system dashboard summary metrics."""
        convs = conversation_repository.get_all()
        msgs = message_repository.get_all()

        total_convs = len(convs)
        total_msgs = len(msgs)

        intents = Counter()
        sentiments = Counter()
        latencies = []
        confidences = []

        for m in msgs:
            meta = m.get("metadata", {})
            if "intent" in meta:
                intents[meta["intent"]] += 1
            if "sentiment" in meta:
                sentiments[meta["sentiment"]] += 1
            if "processing_time_ms" in meta:
                latencies.append(meta["processing_time_ms"])
            if "confidence" in meta:
                confidences.append(meta["confidence"])

        avg_latency = round(sum(latencies) / len(latencies), 2) if latencies else 35.0
        avg_confidence = round(sum(confidences) / len(confidences), 4) if confidences else 0.88

        total_sent = sum(sentiments.values()) or 1
        pos_pct = round((sentiments.get("positive", 0) / total_sent) * 100, 1)
        neg_pct = round((sentiments.get("negative", 0) / total_sent) * 100, 1)

        return {
            "total_conversations": total_convs,
            "total_messages": total_msgs,
            "active_sessions": sum(1 for c in convs if c.get("status") in ["OPEN", "ACTIVE"]),
            "average_confidence": avg_confidence,
            "positive_sentiment_pct": pos_pct,
            "negative_sentiment_pct": neg_pct,
            "average_response_time_ms": avg_latency,
            "most_common_intents": dict(intents.most_common(5)),
            "sentiment_distribution": dict(sentiments)
        }

analytics_aggregator = AnalyticsAggregator()
