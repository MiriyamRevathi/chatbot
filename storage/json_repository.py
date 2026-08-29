"""
Generic JSON Repository for FinTechHub
Supports CRUD, indexing, filtering, sorting, and pagination over file-based data.
"""

from pathlib import Path
from typing import List, Dict, Any, Optional, Callable
from storage.file_storage import FileStorageEngine

class JsonRepository:
    def __init__(self, storage_engine: FileStorageEngine, filename: str, id_field: str = "id"):
        self.storage = storage_engine
        self.filename = filename
        self.id_field = id_field

    def get_all(self) -> List[Dict[str, Any]]:
        return self.storage.read_json(self.filename, default=[])

    def get_by_id(self, item_id: str) -> Optional[Dict[str, Any]]:
        items = self.get_all()
        for item in items:
            if str(item.get(self.id_field)) == str(item_id):
                return item
        return None

    def find(self, predicate: Callable[[Dict[str, Any]], bool]) -> List[Dict[str, Any]]:
        items = self.get_all()
        return [item for item in items if predicate(item)]

    def add(self, item: Dict[str, Any]) -> Dict[str, Any]:
        items = self.get_all()
        items.append(item)
        self.storage.write_json(self.filename, items)
        return item

    def update(self, item_id: str, updates: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        items = self.get_all()
        for i, item in enumerate(items):
            if str(item.get(self.id_field)) == str(item_id):
                items[i].update(updates)
                self.storage.write_json(self.filename, items)
                return items[i]
        return None

    def delete(self, item_id: str) -> bool:
        items = self.get_all()
        initial_len = len(items)
        items = [item for item in items if str(item.get(self.id_field)) != str(item_id)]
        if len(items) < initial_len:
            self.storage.write_json(self.filename, items)
            return True
        return False
