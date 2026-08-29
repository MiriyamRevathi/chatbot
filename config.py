"""
ChatFlow Application Configuration and Knowledge Dictionary.
Provides comprehensive configuration settings, default intents, training corpora, and system constants.
"""

import os
from pathlib import Path

class Config:
    """Master Application Configuration."""

    # Project Directories
    BASE_DIR = Path(__file__).resolve().parent
    DATA_DIR = os.path.join(BASE_DIR, "data")
    ARTIFACTS_DIR = os.path.join(BASE_DIR, "artifacts")
    LOGS_DIR = os.path.join(BASE_DIR, "logs")

    # Security Configuration
    SECRET_KEY = os.environ.get("SECRET_KEY", "chatflow-secret-key-production-safe-demo-2026")
    SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT", "chatflow-salt-998877")
    SESSION_TIMEOUT_MINUTES = 120
    TOKEN_EXPIRATION_HOURS = 24

    # System Performance & Confidence Thresholds
    HUMAN_ESCALATION_THRESHOLD = 0.65
    HIGH_CONFIDENCE_THRESHOLD = 0.85
    DEFAULT_TOP_K_KNOWLEDGE = 3
    MAX_CONVERSATION_HISTORY = 20

    # User Roles
    ROLE_USER = "USER"
    ROLE_SUPPORT_AGENT = "SUPPORT_AGENT"
    ROLE_ML_ENGINEER = "ML_ENGINEER"
    ROLE_ADMIN = "ADMIN"

    ALL_ROLES = [ROLE_USER, ROLE_SUPPORT_AGENT, ROLE_ML_ENGINEER, ROLE_ADMIN]

    # Conversation Statuses
    STATUS_OPEN = "OPEN"
    STATUS_ACTIVE = "ACTIVE"
    STATUS_RESOLVED = "RESOLVED"
    STATUS_ESCALATED = "ESCALATED"
    STATUS_ARCHIVED = "ARCHIVED"

    # Default Intent Training Dataset Definitions (15+ Intents)
    INTENT_DATASET = {
        "greeting": [
            "hello", "hi", "hey", "good morning", "good afternoon", "good evening",
            "greetings", "howdy", "hi there", "hello assistant", "hey chatflow",
            "welcome", "starting conversation", "hi chatbot", "salutations"
        ],
        "goodbye": [
            "bye", "goodbye", "see you later", "farewell", "talk to you later",
            "have a good day", "exit", "quit", "closing chat", "bye for now",
            "end conversation", "thanks bye", "catch you later"
        ],
        "help": [
            "help", "can you help me", "i need assistance", "support needed",
            "what can you do", "show me options", "help menu", "guidance required",
            "how does this work", "assist me please", "i am stuck", "need help"
        ],
        "billing": [
            "invoice", "billing issue", "charge on my card", "payment receipt",
            "payment failure", "double charge", "bill question", "where is my invoice",
            "update credit card", "payment method", "billing department", "bank statement"
        ],
        "refund": [
            "i want a refund", "refund status", "money back request", "cancel payment refund",
            "how to get refund", "return item refund", "reimbursement", "wrong charge refund",
            "dispute charge", "refund policy", "claim refund"
        ],
        "order_status": [
            "where is my order", "order status", "track package", "shipping update",
            "delivery delay", "order tracking", "has my order shipped", "package arrival",
            "order number lookup", "estimated delivery date"
        ],
        "technical_support": [
            "system error", "bug report", "app crashing", "connection error",
            "not working", "technical issue", "page failed to load", "api error",
            "performance issue", "broken button", "500 internal error", "timeout error"
        ],
        "account": [
            "account settings", "profile update", "change email", "delete account",
            "account information", "user profile", "update address", "view my account",
            "manage profile", "account tier", "linked accounts"
        ],
        "password": [
            "forgot password", "reset password", "change password", "password policy",
            "unable to login password", "update security credentials", "passcode reset",
            "password expired", "send password reset link"
        ],
        "subscription": [
            "upgrade subscription", "downgrade plan", "cancel plan", "renew membership",
            "subscription status", "enterprise plan", "monthly plan", "annual plan",
            "change subscription", "membership renewal"
        ],
        "pricing": [
            "how much does it cost", "pricing details", "plans cost", "discount available",
            "tier pricing", "free trial", "is there a free plan", "cost breakdown",
            "quotes", "enterprise pricing"
        ],
        "complaint": [
            "unhappy with service", "terrible experience", "poor quality", "dissatisfied",
            "complaint submission", "manager escalation", "unacceptable behavior",
            "frustrated with delay", "horrible support", "bad experience"
        ],
        "feedback": [
            "feature request", "great app", "suggestion for improvement", "feedback submission",
            "i love this feature", "constructive feedback", "product idea", "user rating",
            "recommendation", "praise"
        ],
        "product_information": [
            "tell me about product", "product specifications", "system requirements",
            "compatibility", "what features are included", "documentation",
            "user manual", "integrations", "sdk support"
        ],
        "contact_support": [
            "speak to human", "talk to support agent", "representative", "phone number",
            "support email", "escalate to agent", "human help", "customer service agent",
            "contact details", "live agent"
        ]
    }

    # Intent Response Master Table
    INTENT_RESPONSES = {
        "greeting": "Hello! Welcome to ChatFlow. How can I assist you with your NLP or customer support queries today?",
        "goodbye": "Thank you for visiting ChatFlow! Have a wonderful day, and feel free to reach out anytime.",
        "help": "I can help you with billing, account settings, order status, technical issues, subscriptions, and knowledge base inquiries. What would you like to explore?",
        "billing": "You can view and manage your invoices under Account Settings > Billing. If you notice an unexpected charge, please let us know.",
        "refund": "Refund requests are processed within 3–5 business days according to our terms of service. Would you like me to initiate a refund request for an order?",
        "order_status": "To check your order status, please provide your 8-digit Order ID (e.g., ORD-12345). You can also track your shipment live in your portal.",
        "technical_support": "I am sorry to hear you are experiencing technical difficulties. Could you provide error details or screenshots so our ML/Tech team can resolve it?",
        "account": "Your profile information, security settings, and contact details can be modified in your Account Dashboard.",
        "password": "To reset your password, click 'Forgot Password' on the login screen or visit your Security Settings page.",
        "subscription": "We offer Free, Pro, and Enterprise subscription tiers. You can manage or upgrade your plan in your Account Settings.",
        "pricing": "ChatFlow offers flexible tier pricing starting with a Free Tier. Pro plans start at $29/mo, and Enterprise plans offer custom limits.",
        "complaint": "We sincerely apologize for your negative experience. I have flagged this conversation for high-priority support agent review.",
        "feedback": "Thank you for sharing your feedback! Our product team regularly reviews user suggestions to improve ChatFlow.",
        "product_information": "ChatFlow is an advanced NLP and Chatbot platform supporting intent classification, sentiment analysis, custom models, and knowledge retrieval.",
        "contact_support": "I am transferring your request to a live support agent. An agent will be with you shortly."
    }

    # Demo Accounts Configuration
    DEMO_ACCOUNTS = [
        {"email": "user@chatflow.local", "name": "Standard User", "role": "USER", "password": "UserPass123!"},
        {"email": "agent@chatflow.local", "name": "Support Agent", "role": "SUPPORT_AGENT", "password": "AgentPass123!"},
        {"email": "engineer@chatflow.local", "name": "ML Engineer", "role": "ML_ENGINEER", "password": "EngineerPass123!"},
        {"email": "admin@chatflow.local", "name": "System Administrator", "role": "ADMIN", "password": "AdminPass123!"}
    ]

    @classmethod
    def init_directories(cls):
        """Ensure all required runtime directories exist."""
        os.makedirs(cls.DATA_DIR, exist_ok=True)
        os.makedirs(cls.ARTIFACTS_DIR, exist_ok=True)
        os.makedirs(cls.LOGS_DIR, exist_ok=True)

# Feature branch update: feature/auth-rbac-system
