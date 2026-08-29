"""
Forecasting Blueprint Routes
"""
from flask import Blueprint, render_template, session, current_app
from security.rbac import RBAC
from ml.forecasting import SpendingForecaster

forecast_bp = Blueprint("forecast", __name__, url_prefix="/forecast")

@forecast_bp.route("/")
@RBAC.require_auth
def index():
    historical_months = [1850.0, 1920.0, 1780.0, 2100.0, 1950.0, 2050.0]
    predictions = SpendingForecaster.forecast_next_months(historical_months, num_months=3)
    return render_template("forecast/index.html", historical=historical_months, predictions=predictions)
