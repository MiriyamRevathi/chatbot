"""
FinTechHub Primary Application Entrypoint & Factory
Initializes Flask app, registers blueprints, configures session storage, error handlers, and Jinja filters.
"""

import os
from flask import Flask, render_template, jsonify
from config import config_by_name

def create_app(config_name: str = "dev") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Register Blueprints
    from routes.auth_routes import auth_bp
    from routes.dashboard_routes import dashboard_bp
    from routes.account_routes import account_bp
    from routes.transaction_routes import transaction_bp
    from routes.budget_routes import budget_bp
    from routes.savings_routes import savings_bp
    from routes.investment_routes import investment_bp
    from routes.loan_routes import loan_bp
    from routes.credit_routes import credit_bp
    from routes.fraud_routes import fraud_bp
    from routes.forecast_routes import forecast_bp
    from routes.segmentation_routes import segmentation_bp
    from routes.report_routes import report_bp
    from routes.admin_routes import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(account_bp)
    app.register_blueprint(transaction_bp)
    app.register_blueprint(budget_bp)
    app.register_blueprint(savings_bp)
    app.register_blueprint(investment_bp)
    app.register_blueprint(loan_bp)
    app.register_blueprint(credit_bp)
    app.register_blueprint(fraud_bp)
    app.register_blueprint(forecast_bp)
    app.register_blueprint(segmentation_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(admin_bp)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("base.html"), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify({"error": "Internal Server Error"}), 500

    return app

if __name__ == "__main__":
    app = create_app("dev")
    app.run(host="127.0.0.1", port=5000, debug=True)
