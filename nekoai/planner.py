from typing import List


class PlanStep:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description


class Planner:
    """Creates simple plans for tasks."""

    def build_plan(self, user_request: str) -> List[PlanStep]:
        request = user_request.lower()
        steps = []

        if any(word in request for word in ["study", "exam", "homework", "learn"]):
            steps = [
                PlanStep("Understand goal", "Identify target topics, deadline, and weak areas."),
                PlanStep("Break topics", "Split the subject into learning blocks."),
                PlanStep("Practice", "Solve exercises and assess progress."),
                PlanStep("Review", "Fix mistakes and reinforce weak points."),
            ]
        elif any(word in request for word in ["code", "build", "script", "app", "project"]):
            steps = [
                PlanStep("Clarify scope", "Define the feature, input, and output requirements."),
                PlanStep("Design architecture", "Choose the structure, modules, and files."),
                PlanStep("Implement", "Write the core code and connect components."),
                PlanStep("Validate", "Run tests, debug issues, and improve quality."),
            ]
        else:
            steps = [
                PlanStep("Identify need", "Clarify what the user wants to achieve."),
                PlanStep("Research", "Gather relevant knowledge and constraints."),
                PlanStep("Execute", "Create the best possible solution."),
                PlanStep("Improve", "Review the result and refine it."),
            ]

        return steps
