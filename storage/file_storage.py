"""
Advanced Local File Storage Engine
Provides JSON document store, CSV table engine, index management, and file-locking mechanics.
"""

import os
import json
import csv
import threading
from pathlib import Path
from typing import Dict, List, Any, Optional

class FileLock:
    def __init__(self, lock_file_path: Path):
        self.lock_file = lock_file_path.with_suffix(".lock")
        self._mutex = threading.Lock()

    def __enter__(self):
        self._mutex.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._mutex.release()

class FileStorageEngine:
    def __init__(self, base_dir: Path):
        self.base_dir = Path(base_dir)
        os.makedirs(self.base_dir, exist_ok=True)
        self._locks: Dict[str, FileLock] = {}

    def _get_lock(self, filename: str) -> FileLock:
        if filename not in self._locks:
            self._locks[filename] = FileLock(self.base_dir / filename)
        return self._locks[filename]

    def read_json(self, filename: str, default: Any = None) -> Any:
        file_path = self.base_dir / filename
        if not file_path.exists():
            return default if default is not None else []
        with self._get_lock(filename):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error reading JSON file {file_path}: {e}")
                return default if default is not None else []

    def write_json(self, filename: str, data: Any) -> bool:
        file_path = self.base_dir / filename
        with self._get_lock(filename):
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, default=str)
                return True
            except Exception as e:
                print(f"Error writing JSON file {file_path}: {e}")
                return False

    def read_csv(self, filename: str) -> List[Dict[str, Any]]:
        file_path = self.base_dir / filename
        if not file_path.exists():
            return []
        with self._get_lock(filename):
            try:
                with open(file_path, "r", encoding="utf-8", newline="") as f:
                    reader = csv.DictReader(f)
                    return [dict(row) for row in reader]
            except Exception as e:
                print(f"Error reading CSV file {file_path}: {e}")
                return []

    def write_csv(self, filename: str, fieldnames: List[str], rows: List[Dict[str, Any]]) -> bool:
        file_path = self.base_dir / filename
        with self._get_lock(filename):
            try:
                with open(file_path, "w", encoding="utf-8", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)
                return True
            except Exception as e:
                print(f"Error writing CSV file {file_path}: {e}")
                return False
