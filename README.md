# FinTechHub — Personal Finance, Risk & Investment Intelligence Platform

FinTechHub is a production-grade, full-stack personal finance, financial risk scoring, and investment intelligence web application built with Python 3.10+, Flask, scikit-learn ML pipelines, ReportLab PDF reporting, and modern Vanilla HTML5/CSS3/JS.

---

## 🌟 Key Features & User Journeys

1. **Authentication & RBAC**: Customer, Financial Analyst, and Administrator role-based access with Werkzeug scrypt password security.
2. **Multi-Account Management**: Simulated Checking, High-Yield Savings, Rewards Credit Cards, and Wealth Investment Accounts.
3. **Transaction Management**: 80+ merchant rule auto-categorization engine, search, filtering, category breakdown, CSV import/export.
4. **Budgeting & Velocity**: Category monthly budgets, spending velocity indicators, and automated budget adjustment recommendations.
5. **Savings Goals**: Emergency fund tracker, vacation goals, and projected target completion date forecasting.
6. **Investment Portfolio**: Stocks, ETFs, Bonds, Gold holdings, asset allocation breakdown, diversification scoring, and live market price simulation.
7. **Loan & EMI Calculator**: Personal, Home, Auto loan calculators, monthly EMI schedule engine, and complete 12-month amortization table previews.
8. **Credit Score Simulator**: Simulated FICO 300-850 credit scoring engine based on 5 weighted credit factors.
9. **ML Fraud Detection**: Scikit-learn Isolation Forest and Local Outlier Factor (LOF) anomaly detection pipeline for transaction fraud alerts.
10. **Spending Forecasting & Segmentation**: Ridge Regression time-series expense predictor and K-Means customer persona clustering.
11. **Financial Risk Engine**: Debt-to-Income (DTI) ratio, liquidity buffer, and 0-100 Financial Health Score.
12. **PDF & Excel Reporting**: Downloadable ReportLab PDF monthly bank-style financial statements.
13. **Admin Monitoring Dashboard**: Platform stats, user management, audit logs, system diagnostics.

---

## 🚀 Installation & Local Setup

### 1. Prerequisites
- Python 3.10 or higher
- Git

### 2. Clone & Setup Virtual Environment
```bash
git clone https://github.com/MiriyamRevathi/fintech.git
cd fintech
python -m venv .venv

# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate
```

### 3. Install Dependencies with Lockfile
```bash
pip install -r requirements.txt
```

### 4. Run Application
```bash
python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000`.

---

## 🔑 Demo Login Accounts

| Role | Username | Password | Access Scope |
|------|----------|----------|--------------|
| **Customer** | `customer` | `Customer123!` | Dashboard, Accounts, Transactions, Budget, Savings, Investments, Loans, Credit |
| **Analyst** | `analyst` | `Analyst123!` | Portfolio Analytics, Fraud Monitoring, Forecasting, Customer Segmentation |
| **Admin** | `admin` | `Admin123!` | User Governance, Audit Logs, System Diagnostics, Fraud Alerts |

---

## 🐳 Docker Deployment

```bash
docker build -t fintechhub .
docker run -p 5000:5000 fintechhub
```

---

## 🧪 Testing

Run the automated pytest suite:
```bash
pytest
```
