"""
ReportLab PDF Financial Statement Generator
Builds downloadable monthly PDF financial statements and portfolio reports.
"""

import os
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

class PDFReportGenerator:
    @staticmethod
    def generate_monthly_statement(output_path: Path, user_name: str, account_summary: dict, transactions: list) -> str:
        doc = SimpleDocTemplate(str(output_path), pagesize=letter)
        styles = getSampleStyleSheet()
        elements = []

        # Title
        title_style = ParagraphStyle("TitleStyle", parent=styles["Heading1"], fontSize=20, leading=24, textColor=colors.HexColor("#1e293b"))
        elements.append(Paragraph(f"FinTechHub — Monthly Statement for {user_name}", title_style))
        elements.append(Spacer(1, 12))

        # Summary Table
        summary_data = [
            ["Metric", "Amount ($)"],
            ["Total Assets", f"${account_summary.get('total_assets', 0.0):,.2f}"],
            ["Total Liabilities", f"${account_summary.get('total_liabilities', 0.0):,.2f}"],
            ["Net Worth", f"${account_summary.get('net_worth', 0.0):,.2f}"]
        ]
        t_summary = Table(summary_data, colWidths=[200, 200])
        t_summary.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f172a')),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('GRID', (0,0), (-1,-1), 0.5, colors.grey)
        ]))
        elements.append(t_summary)
        elements.append(Spacer(1, 20))

        doc.build(elements)
        return str(output_path)
