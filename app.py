"""
ChatFlow Application Factory and Server Entry Point.
"""

from flask import Flask, render_template, jsonify
from config import Config
from core.exceptions import ChatFlowException
from repositories.user_repository import user_repository
from repositories.knowledge_repository import knowledge_repository
from repositories.model_repository import model_repository

# Import Blueprints
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.chat_routes import chat_bp
from routes.knowledge_routes import knowledge_bp
from routes.nlp_lab_routes import nlp_lab_bp
from routes.model_playground_routes import model_playground_bp
from routes.analytics_routes import analytics_bp
from routes.admin_routes import admin_bp
from routes.diagnostics_routes import diagnostics_bp

from api.api_auth import api_auth_bp
from api.api_chat import api_chat_bp
from api.api_nlp import api_nlp_bp
from api.api_knowledge import api_kb_bp
from api.api_models import api_models_bp
from api.api_experiments import api_exp_bp
from api.api_analytics import api_analytics_bp
from api.api_feedback import api_feedback_bp
from api.api_diagnostics import api_diag_bp

def create_app(config_class=Config):
    """Flask Application Factory."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize runtime storage directories
    config_class.init_directories()

    # Register UI Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(knowledge_bp)
    app.register_blueprint(nlp_lab_bp)
    app.register_blueprint(model_playground_bp)
    app.register_blueprint(analytics_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(diagnostics_bp)

    # Register API Blueprints
    app.register_blueprint(api_auth_bp)
    app.register_blueprint(api_chat_bp)
    app.register_blueprint(api_nlp_bp)
    app.register_blueprint(api_kb_bp)
    app.register_blueprint(api_models_bp)
    app.register_blueprint(api_exp_bp)
    app.register_blueprint(api_analytics_bp)
    app.register_blueprint(api_feedback_bp)
    app.register_blueprint(api_diag_bp)

    # Error Handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template("500.html"), 500

    @app.errorhandler(ChatFlowException)
    def handle_chatflow_exception(e):
        return jsonify(e.to_dict()), e.status_code

    return app

if __name__ == "__main__":
    app = create_app()
    print("============================================================")
    print("CHATFLOW — AI CHATBOT & NLP PLATFORM")
    print("Starting production server on http://127.0.0.1:5000")
    print("============================================================")
    app.run(host="127.0.0.1", port=5000, debug=False)
