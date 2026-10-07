from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class BaseAgent:
    name: str
    description: str = "General agent"

    def handle(self, request: str, context: Dict[str, Any]) -> str:
        return f"{self.name} is ready to help with: {request}"


class CodingAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Coding Agent", description="Generates code, fixes bugs, explains programming concepts, reviews projects")

    def handle(self, request: str, context: Dict[str, Any]) -> str:
        return (
            "I can generate code, fix bugs, explain concepts, and review projects. "
            f"For '{request}', I would first clarify the stack, goals, and expected output."
        )


class LearningAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Learning Agent", description="Builds study plans, quizzes, worksheets, and learning routines")

    def handle(self, request: str, context: Dict[str, Any]) -> str:
        return (
            "I can create study plans, quizzes, worksheets, and teach difficult concepts step by step. "
            f"For '{request}', I would break the topic into smaller lessons and practice tasks."
        )


class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Research Agent", description="Research topics, analyze options, compare technologies, summarize findings")

    def handle(self, request: str, context: Dict[str, Any]) -> str:
        return (
            "I can research topics, compare technologies, and summarize what matters most. "
            f"For '{request}', I would gather the essential facts and then recommend the best path."
        )


class WebsiteAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Website Agent", description="Builds websites, APIs, dashboards, databases, and full-stack products")

    def handle(self, request: str, context: Dict[str, Any]) -> str:
        return (
            "I can design websites, APIs, databases, dashboards, and full-stack apps. "
            f"For '{request}', I would begin with the product scope, architecture, and user flow."
        )


class RobloxAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Roblox Agent", description="Creates Lua scripts, UI, game systems, NPC AI, weapons, and economy systems")

    def handle(self, request: str, context: Dict[str, Any]) -> str:
        return (
            "I can create Lua scripts, NPC behavior, game systems, UI, weapons, and economy loops. "
            f"For '{request}', I would design the game loop and core mechanics first."
        )


class UnrealAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Unreal Engine Agent", description="Helps with gameplay logic, UI, level design, and gameplay systems")

    def handle(self, request: str, context: Dict[str, Any]) -> str:
        return (
            "I can help with gameplay logic, UI systems, level ideas, and game architecture. "
            f"For '{request}', I would break it into systems and build a clean implementation plan."
        )


__all__ = [
    "BaseAgent",
    "CodingAgent",
    "LearningAgent",
    "ResearchAgent",
    "WebsiteAgent",
    "RobloxAgent",
    "UnrealAgent",
]
