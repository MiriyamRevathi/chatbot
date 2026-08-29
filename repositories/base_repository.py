"""
Thread-safe Atomic File Persistence Repository Base Class.
Provides robust JSON file-based persistence with fallback recovery.
"""

import os
import json
import threading
from config import Config
from core.exceptions import StorageError

class BaseRepository:
    """Generic File-based Repository Base Class."""

    def __init__(self, filename: str):
        Config.init_directories()
        self.filepath = os.path.join(Config.DATA_DIR, filename)
        self._lock = threading.Lock()
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Create file with empty list if missing."""
        if not os.path.exists(self.filepath):
            self._write_all([])

    def _read_all(self) -> list:
        """Read all JSON records from disk safely."""
        with self._lock:
            if not os.path.exists(self.filepath):
                return []
            try:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                # Attempt recovery or return empty list
                return []

    def _write_all(self, data: list):
        """Atomically write JSON records to disk."""
        with self._lock:
            temp_path = self.filepath + ".tmp"
            try:
                with open(temp_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                os.replace(temp_path, self.filepath)
            except Exception as e:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                raise StorageError(f"Failed writing data to {self.filepath}: {str(e)}")

    def get_all(self) -> list:
        """Get all entities."""
        return self._read_all()

    def find_by_id(self, item_id: str, id_field="id") -> dict:
        """Find single entity by ID."""
        records = self._read_all()
        for r in records:
            if str(r.get(id_field)) == str(item_id):
                return r
        return None

    def save(self, item: dict, id_field="id") -> dict:
        """Insert or update entity in storage."""
        records = self._read_all()
        item_id = item.get(id_field)

        if not item_id:
            raise StorageError(f"Item missing ID field '{id_field}'")

        existing_index = None
        for idx, r in enumerate(records):
            if str(r.get(id_field)) == str(item_id):
                existing_index = idx
                break

        if existing_index is not None:
            records[existing_index] = item
        else:
            records.append(item)

        self._write_all(records)
        return item

    def delete(self, item_id: str, id_field="id") -> bool:
        """Delete entity by ID."""
        records = self._read_all()
        initial_count = len(records)
        records = [r for r in records if str(r.get(id_field)) != str(item_id)]
        if len(records) < initial_count:
            self._write_all(records)
            return True
        return False
