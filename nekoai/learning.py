from __future__ import annotations

from typing import Dict, List


class LearningEngine:
    """Stores lessons from each interaction for future improvement."""

    def __init__(self, memory):
        self.memory = memory

    def record(self, request: str, result: str) -> str:
        if not request:
            return "No learning data recorded."
        self.memory.add_conversation(request, result)
        self.memory.remember("last_learning_topic", request)
        return "Learning engine updated with this interaction."

    def summarize_patterns(self) -> Dict[str, List[str]]:
        conversations = self.memory.data.get("conversations", [])
        topics = [item.get("user", "") for item in conversations]
        return {"topics": topics}


__all__ = ["LearningEngine"]
