"""
Dynamic Runtime Configuration Manager.
"""

from config import Config
import threading

class ConfigManager:
    """Runtime Configuration Property Manager."""

    def __init__(self):
        self._lock = threading.Lock()
        self._overrides = {}

    def get(self, key: str, default=None):
        """Retrieve config value with runtime override check."""
        with self._lock:
            if key in self._overrides:
                return self._overrides[key]
        return getattr(Config, key, default)

    def set(self, key: str, value):
        """Set a runtime override config parameter."""
        with self._lock:
            self._overrides[key] = value

    def reset(self):
        """Reset all runtime overrides."""
        with self._lock:
            self._overrides.clear()

config_manager = ConfigManager()
