# ChatFlow — AI Chatbot & NLP Platform

ChatFlow is an enterprise-grade, full-stack, local AI chatbot and natural language processing (NLP) management platform built with Python 3.10+, Flask, scikit-learn, and Vanilla JavaScript.

The platform provides a complete ecosystem for end-users, support agents, ML engineers, and system administrators, featuring ChatGPT-style interactive chat, intent classification, hybrid sentiment analysis, named entity extraction, BM25 & TF-IDF document retrieval, an interactive NLP Lab, an ML Model Playground, experiment tracking, executive analytics, and real-time system diagnostics.

---

## Key Features

- **Interactive ChatGPT-Style Interface**: Real-time multi-turn messaging, intent & sentiment badges, confidence scores, processing latency tracking, conversation search, and thread export.
- **Local ML & NLP Engine**: Built-in TF-IDF vectorization, Multinomial Naive Bayes, Logistic Regression, Decision Trees, Support Vector Machines, Porter Stemmer, Dictionary Lemmatizer, RAKE keyword extraction, and TextRank summarization.
- **Hybrid Sentiment Analysis**: Combined lexicon (VADER-style) and machine learning sentiment analyzer returning polarity, numerical scores (-1.0 to +1.0), and emotion breakdowns.
- **Named Entity Recognition (NER)**: Pattern-based regex extraction (emails, order IDs, account numbers, URLs, dates, currencies) combined with domain gazetteers.
- **Knowledge Base Retrieval**: Hybrid document search engine combining Okapi BM25 ranking and TF-IDF vector cosine similarity for knowledge article matching.
- **Human Escalation Workflow**: Priority queue routing when chatbot confidence drops below configurable threshold (default: 0.65).
- **ML Model Playground**: Interface for training, grid search hyperparameter tuning, evaluating accuracy/F1/confusion matrices, and joblib artifact persistence.
- **Experiment Tracking**: Experiment run logging, parameter comparison, and metrics delta evaluation.
- **Role-Based Access Control (RBAC)**: Fine-grained permissions across four roles (`USER`, `SUPPORT_AGENT`, `ML_ENGINEER`, `ADMIN`).
- **System Telemetry & Diagnostics**: Dedicated `/diagnostics` endpoint with real-time uptime, memory, storage, and model health status.

---

## Technology Stack

- **Backend**: Python 3.10+, Flask, Werkzeug, Jinja2
- **Machine Learning & NLP**: scikit-learn, numpy, pandas, joblib, matplotlib, custom algorithm suite
- **Frontend**: Responsive HTML5, modular CSS3 (CSS custom properties, Light/Dark mode themes), Vanilla JavaScript modules
- **Storage**: Atomic file-based repository system (JSON/CSV) with optional SQLite compatibility layer
- **Testing & Packaging**: pytest test suite, pyproject.toml, requirements.txt, poetry.lock, requirements.lock, Dockerfile

---

## Demo Accounts

The application automatically seeds safe demo accounts upon launch:

| Role | Email | Password | Access Capabilities |
|---|---|---|---|
| **Standard User** | `user@chatflow.local` | `UserPass123!` | Chat interface, Knowledge Base search, Feedback ratings |
| **Support Agent** | `agent@chatflow.local` | `AgentPass123!` | Conversation takeover, Notes, Escalation queue, Knowledge management |
| **ML Engineer** | `engineer@chatflow.local` | `EngineerPass123!` | NLP Lab, Model Playground, Experiment tracking, Model training |
| **Administrator** | `admin@chatflow.local` | `AdminPass123!` | Full platform access, User management, Audit logs, Diagnostics |

---

## Quick Start & Installation

### Standard Installation

```bash
# 1. Clone or navigate to the repository
cd chatflow

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Deterministic / Locked Installation

```bash
# Install using pinned lockfile via pip
pip install -r requirements.lock

# OR using Poetry
poetry install
```

---

## Running the Application

Start the production Flask server:

```bash
python app.py
```

The web application will be accessible in your browser at:
`http://127.0.0.1:5000`

---

## Running Tests

Execute the comprehensive pytest suite:

```bash
# Run pytest suite across all 10 test modules
pytest

# Run tests with verbose output
pytest -v
```

---

## Docker Instructions

Build and run the application inside a container:

```bash
# 1. Build Docker image
docker build -t chatflow .

# 2. Run container on port 5000
docker run -p 5000:5000 chatflow
```

---

## Project Structure

```
chatflow/
├── app.py                      # Application factory & server entry point
├── config.py                   # Configuration, secrets, intent definitions
├── pyproject.toml              # Modern Python packaging configuration
├── requirements.txt            # Dependency manifest
├── requirements.lock           # Deterministic pip lockfile
├── poetry.lock                 # Standard Poetry lockfile
├── Dockerfile                  # Container execution blueprint
├── README.md                   # Complete documentation
├── core/                       # Core system utilities (logging, security, cache, validator)
├── auth/                       # Authentication, session manager, RBAC decorators
├── nlp/                        # Local NLP engine, classifiers, preprocessors, corpora
├── chatbot/                    # Response engine, policy engine, dialogue trees, escalation
├── knowledge/                  # Article service, vector store, BM25 document search
├── models/                     # Model trainer, metrics calculator, joblib registry
├── experiments/                # Experiment tracking and run logger
├── analytics/                  # Metrics aggregator and report generator
├── feedback/                   # User ratings and satisfaction scorer
├── monitoring/                 # Diagnostics service and health checker
├── repositories/               # Atomic JSON/CSV data repositories
├── routes/                     # UI view controllers (Flask Blueprints)
├── api/                        # REST API endpoints
├── templates/                  # Modular Jinja2 HTML templates
├── static/                     # CSS stylesheets & modular JS scripts
└── tests/                      # Pytest test suite (10 test modules)
```

---

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/api/health` | GET | Basic system health check |
| `/api/diagnostics` | GET | System telemetry and diagnostics |
| `/api/auth/login` | POST | Authenticate user credentials |
| `/api/auth/register` | POST | Register new user account |
| `/api/chat` | POST | Process chat message and return bot response |
| `/api/conversations` | GET / POST | Manage multi-turn conversation sessions |
| `/api/nlp/analyze` | POST | Run full live NLP dissection on raw text |
| `/api/knowledge` | GET / POST | Search or create knowledge base articles |
| `/api/models` | GET | List registered ML models |
| `/api/models/train` | POST | Train and save new model artifact |
| `/api/experiments` | GET | List ML experiment runs |
| `/api/analytics` | GET | Fetch platform summary metrics |
| `/api/feedback` | POST | Submit helpfulness rating for message |

---

## License

Proprietary — All rights reserved.
