"""
Structured Logging Configuration.
"""

import os
import logging
import json
from datetime import datetime
from config import Config

class JSONFormatter(logging.Formatter):
    """JSON log formatter for structured audit trails."""

    def format(self, record):
        log_obj = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "line": record.lineno
        }
        if hasattr(record, "user_id"):
            log_obj["user_id"] = record.user_id
        if record.exc_info:
            log_obj["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_obj)

def setup_logger(name="chatflow", log_level=logging.INFO):
    """Configure and return structured logger."""
    Config.init_directories()
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.propagate = False

    if not logger.handlers:
        # Console handler
        c_handler = logging.StreamHandler()
        c_handler.setLevel(log_level)
        c_format = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s")
        c_handler.setFormatter(c_format)
        logger.addHandler(c_handler)

        # File JSON handler
        file_path = os.path.join(Config.LOGS_DIR, "chatflow.jsonl")
        f_handler = logging.FileHandler(file_path, encoding="utf-8")
        f_handler.setLevel(log_level)
        f_handler.setFormatter(JSONFormatter())
        logger.addHandler(f_handler)

    return logger

logger = setup_logger()
