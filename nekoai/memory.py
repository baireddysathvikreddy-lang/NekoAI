from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class MemoryStore:
    """Simple persistent memory layer for NekoAI."""

    def __init__(self, path: str = "memory/nekoai_memory.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.data: Dict[str, Any] = self._load()

    def _load(self) -> Dict[str, Any]:
        default = {
            "owner_name": "Owner",
            "preferences": {},
            "projects": [],
            "conversations": [],
            "goals": [],
            "learning_progress": {},
            "coding_projects": [],
            "website_projects": [],
            "game_projects": [],
        }

        if not self.path.exists():
            return default

        try:
            with self.path.open("r", encoding="utf-8") as handle:
                loaded = json.load(handle)
                if isinstance(loaded, dict):
                    for key, value in default.items():
                        loaded.setdefault(key, value)
                    return loaded
        except (json.JSONDecodeError, OSError):
            pass

        return default

    def save(self) -> None:
        with self.path.open("w", encoding="utf-8") as handle:
            json.dump(self.data, handle, indent=2, ensure_ascii=False)

    def set_owner_name(self, name: str) -> None:
        self.data["owner_name"] = name
        self.save()

    def remember(self, key: str, value: Any) -> None:
        self.data[key] = value
        self.save()

    def add_conversation(self, user_message: str, assistant_response: str) -> None:
        self.data.setdefault("conversations", []).append({
            "user": user_message,
            "assistant": assistant_response,
        })
        self.save()

    def add_goal(self, goal: str) -> None:
        self.data.setdefault("goals", []).append(goal)
        self.save()

    def add_project(self, project_name: str, project_type: str) -> None:
        entry = {"name": project_name, "type": project_type}
        project_key = {
            "coding": "coding_projects",
            "website": "website_projects",
            "game": "game_projects",
        }.get(project_type, "projects")
        self.data.setdefault(project_key, []).append(entry)
        self.save()

    def get_summary(self) -> Dict[str, Any]:
        return self.data


__all__ = ["MemoryStore"]
