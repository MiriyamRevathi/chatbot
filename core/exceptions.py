"""
Custom Exception Hierarchy for ChatFlow.
"""

class ChatFlowException(Exception):
    """Base exception for all ChatFlow application errors."""
    def __init__(self, message="An internal application error occurred", status_code=500, payload=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.payload = payload or {}

    def to_dict(self):
        rv = dict(self.payload)
        rv["error"] = self.message
        rv["status_code"] = self.status_code
        return rv

class AuthenticationError(ChatFlowException):
    """Raised when authentication credentials or tokens are invalid."""
    def __init__(self, message="Authentication failed", status_code=401):
        super().__init__(message, status_code=status_code)

class AuthorizationError(ChatFlowException):
    """Raised when a user lacks required permissions."""
    def __init__(self, message="Access denied", status_code=403):
        super().__init__(message, status_code=status_code)

class NotFoundError(ChatFlowException):
    """Raised when a requested resource does not exist."""
    def __init__(self, message="Resource not found", status_code=404):
        super().__init__(message, status_code=status_code)

class ValidationError(ChatFlowException):
    """Raised when input validation fails."""
    def __init__(self, message="Invalid request parameters", status_code=422, errors=None):
        payload = {"validation_errors": errors} if errors else {}
        super().__init__(message, status_code=status_code, payload=payload)

class NLPError(ChatFlowException):
    """Raised when NLP parsing or model prediction fails."""
    def __init__(self, message="NLP processing failure", status_code=500):
        super().__init__(message, status_code=status_code)

class ModelError(ChatFlowException):
    """Raised when model training, loading, or serialization fails."""
    def __init__(self, message="ML model error", status_code=500):
        super().__init__(message, status_code=status_code)

class StorageError(ChatFlowException):
    """Raised when repository atomic IO fails."""
    def __init__(self, message="Storage operation failed", status_code=500):
        super().__init__(message, status_code=status_code)
