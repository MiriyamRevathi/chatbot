"""
In-Memory LRU Cache with Time-To-Live (TTL) Support.
"""

import time
import threading

class Cache:
    """Thread-safe LRU Cache with TTL."""

    def __init__(self, maxsize=500, ttl=300):
        self.maxsize = maxsize
        self.ttl = ttl
        self._store = {}
        self._lock = threading.Lock()

    def get(self, key):
        """Get value from cache if valid."""
        with self._lock:
            if key not in self._store:
                return None
            val, expiry = self._store[key]
            if time.time() > expiry:
                del self._store[key]
                return None
            return val

    def set(self, key, value, custom_ttl=None):
        """Set value in cache with TTL."""
        ttl = custom_ttl if custom_ttl is not None else self.ttl
        expiry = time.time() + ttl
        with self._lock:
            if len(self._store) >= self.maxsize and key not in self._store:
                # Evict oldest entry
                oldest_key = min(self._store.keys(), key=lambda k: self._store[k][1])
                del self._store[oldest_key]
            self._store[key] = (value, expiry)

    def clear(self):
        """Clear all cached entries."""
        with self._lock:
            self._store.clear()

global_cache = Cache()
