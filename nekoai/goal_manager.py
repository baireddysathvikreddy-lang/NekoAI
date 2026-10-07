from __future__ import annotations

from typing import List, Optional


class GoalManager:
    """Tracks the owner's current objectives and priorities."""

    def __init__(self):
        self.goals: List[str] = []

    def add_goal(self, goal: str) -> None:
        if goal not in self.goals:
            self.goals.append(goal)

    def extract_goal(self, request: str) -> str:
        request = request.strip()
        if not request:
            return "General assistance"
        return request

    def current_goals(self) -> List[str]:
        return self.goals

    def prioritize(self, request: str) -> str:
        goal = self.extract_goal(request)
        self.add_goal(goal)
        return f"Priority goal set: {goal}"


__all__ = ["GoalManager"]
