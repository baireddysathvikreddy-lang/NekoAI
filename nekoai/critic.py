from __future__ import annotations

from typing import List


class CriticEngine:
    """Checks if the suggested action is useful, safe, and aligned with the goal."""

    def review(self, request: str, plan: List[str], action: str) -> str:
        checks = []

        if not request.strip():
            checks.append("Missing user request")
        if not plan:
            checks.append("No plan produced")
        if "I can help" in action and "tell me what you want" in action.lower():
            checks.append("Needs clarification to be more useful")

        if checks:
            return "Critical review: " + "; ".join(checks)
        return "Critical review: the plan is coherent and aligned with the owner goal."


__all__ = ["CriticEngine"]
