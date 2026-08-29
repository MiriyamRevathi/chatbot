"""
Analytics Report Summary Generator.
"""

from analytics.aggregator import analytics_aggregator

class ReportGenerator:
    """Generates structured analytics reports."""

    def generate_report(self) -> dict:
        """Generate comprehensive analytics report."""
        summary = analytics_aggregator.get_summary_metrics()
        report = {
            "title": "ChatFlow Executive Analytics Summary",
            "metrics": summary,
            "status": "HEALTHY"
        }
        return report

report_generator = ReportGenerator()
