from dataclasses import dataclass, field
from pathlib import Path
import json
from typing import Any, Dict, List


@dataclass
class MemoryEntry:
    key: str
    value: Any
    created_at: str
    updated_at: str


class MemoryStore:
    """Simple persistent memory layer for NekoAI."""

    def __init__(self, path: str = "memory/nekoai_memory.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.data: Dict[str, Any] = self._load()

    def _load(self) -> Dict[str, Any]:
        if not self.path.exists():
            return {
                "owner_name": "User",
                "preferences": {},
                "projects": [],
                "conversations": [],
                "goals": [],
                "learning_progress": {},
                "coding_projects": [],
                "website_projects": [],
                "game_projects": [],
            }

        try:
            with self.path.open("r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return {
                "owner_name": "User",
                "preferences": {},
                "projects": [],
                "conversations": [],
                "goals": [],
                "learning_progress": {},
                "coding_projects": [],
                "website_projects": [],
                "game_projects": [],
            }

    def save(self) -> None:
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

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
        key = {
            "coding": "coding_projects",
            "website": "website_projects",
            "game": "game_projects",
        }.get(project_type, "projects")
        self.data.setdefault(key, []).append(entry)
        self.save()

    def get_summary(self) -> Dict[str, Any]:
        return self.data
