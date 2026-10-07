from __future__ import annotations

from typing import List


class KnowledgeBase:
    """Local knowledge base for NekoAI."""

    def __init__(self):
        self.categories = {
            "programming": [
                "python", "javascript", "typescript", "lua", "csharp", "java", "go", "rust",
                "debugging", "algorithms", "data structures", "testing",
            ],
            "ai": [
                "artificial intelligence", "machine learning", "llm", "agents", "reasoning",
                "planning", "memory", "knowledge", "neural networks",
            ],
            "web": [
                "html", "css", "react", "api", "database", "backend", "frontend",
                "full stack", "django", "fastapi", "express",
            ],
            "game_dev": [
                "roblox", "lua", "unreal engine", "game design", "npc", "ui", "economy systems",
                "weapon systems", "level design",
            ],
            "study": [
                "mathematics", "science", "history", "languages", "research", "exams",
                "study plans", "worksheets", "quizzes",
            ],
        }

    def search(self, query: str) -> List[str]:
        q = query.lower()
        matches: List[str] = []
        for category, keywords in self.categories.items():
            if any(keyword in q for keyword in keywords):
                matches.append(category)
        return matches or ["general"]

    def explain(self, query: str) -> str:
        matches = self.search(query)
        if matches == ["general"]:
            return "This is a general request. I can help with coding, knowledge, research, study planning, and game development."
        return f"Relevant knowledge areas: {', '.join(matches)}."


__all__ = ["KnowledgeBase"]
