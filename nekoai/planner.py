from dataclasses import dataclass
from typing import List


@dataclass
class PlanStep:
    title: str
    description: str


class Planner:
    """Creates simple structured plans based on user intent."""

    def build_plan(self, user_request: str) -> List[PlanStep]:
        request = user_request.lower()

        if any(word in request for word in ["study", "exam", "learn", "math", "science", "school", "quiz", "homework"]):
            return [
                PlanStep("Clarify goal", "Identify the subject, difficulty level, and due date."),
                PlanStep("Break topics", "Split the subject into smaller learning units."),
                PlanStep("Practice", "Solve exercises, take notes, and review mistakes."),
                PlanStep("Improve", "Repeat weak areas and test understanding before finishing."),
            ]

        if any(word in request for word in ["code", "build", "script", "app", "debug", "project", "program"]):
            return [
                PlanStep("Define scope", "Clarify what the product should do and what success looks like."),
                PlanStep("Design", "Choose the architecture, data flow, and files required."),
                PlanStep("Implement", "Write the actual code and connect the pieces."),
                PlanStep("Validate", "Run checks, fix issues, and improve the final result."),
            ]

        if any(word in request for word in ["website", "api", "backend", "frontend", "dashboard", "database"]):
            return [
                PlanStep("Outline experience", "Map the user flow and system requirements."),
                PlanStep("Select stack", "Choose frameworks, storage, and deployment strategy."),
                PlanStep("Build core", "Create the app structure and main features."),
                PlanStep("Refine", "Review performance, security, and usability."),
            ]

        if any(word in request for word in ["roblox", "lua", "game", "npc", "weapon", "economy"]):
            return [
                PlanStep("Design gameplay", "Define the game loop, core activity, and rewards."),
                PlanStep("Create systems", "Build player logic, UI, enemies, and progression."),
                PlanStep("Tune balance", "Adjust difficulty, rewards, and interaction feel."),
                PlanStep("Polish", "Improve visuals, feedback, and replay value."),
            ]

        return [
            PlanStep("Understand need", "Clarify the user goal and required outcome."),
            PlanStep("Research", "Gather relevant information and compare options."),
            PlanStep("Execute", "Apply the best approach and build the solution."),
            PlanStep("Review", "Check quality and improve the final result."),
        ]


__all__ = ["PlanStep", "Planner"]
