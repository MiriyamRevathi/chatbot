"""
Analytics Dashboard Backend Service.
"""

from analytics.aggregator import analytics_aggregator
from analytics.report_generator import report_generator

class AnalyticsService:
    """High level service providing analytics data."""

    def get_dashboard_stats(self) -> dict:
        """Get analytics dashboard stats."""
        return analytics_aggregator.get_summary_metrics()

    def get_report() -> dict:
        """Get formatted analytics report."""
        return report_generator.generate_report()

analytics_service = AnalyticsService()
