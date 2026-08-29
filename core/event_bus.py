"""
In-Memory Event Bus for Asynchronous Decoupled Event Dispatching.
"""

from collections import defaultdict
import threading
from core.logging_config import logger

class EventBus:
    """Thread-safe event pub/sub manager."""
    def __init__(self):
        self._subscribers = defaultdict(list)
        self._lock = threading.Lock()

    def subscribe(self, event_type: str, handler_fn):
        """Subscribe handler function to an event type."""
        with self._lock:
            self._subscribers[event_type].append(handler_fn)

    def publish(self, event_type: str, payload: dict = None):
        """Publish event to all registered subscribers."""
        payload = payload or {}
        with self._lock:
            handlers = list(self._subscribers.get(event_type, []))

        for handler in handlers:
            try:
                handler(payload)
            except Exception as e:
                logger.error(f"Error handling event {event_type} in {handler.__name__}: {str(e)}")

event_bus = EventBus()
