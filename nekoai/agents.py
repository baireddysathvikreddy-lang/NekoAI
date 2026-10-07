from typing import Dict, List


class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    def handle(self, request: str, context: Dict) -> str:
        return f"{self.name} is ready to assist with: {request}"


class CodingAgent(BaseAgent):
    def __init__(self):
        super().__init__("Coding Agent")

    def handle(self, request: str, context: Dict) -> str:
        return (
            "I can generate code, explain concepts, fix bugs, and plan software projects. "
            f"For request: '{request}' I would start by clarifying the tech stack and requirements."
        )


class LearningAgent(BaseAgent):
    def __init__(self):
        super().__init__("Learning Agent")

    def handle(self, request: str, context: Dict) -> str:
        return (
            "I can build study plans, create quizzes, and explain difficult topics in a simple way. "
            f"For: '{request}' I would break it into lessons and practice tasks."
        )


class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("Research Agent")

    def handle(self, request: str, context: Dict) -> str:
        return (
            "I can summarize research topics and compare technologies. "
            f"For: '{request}' I would gather facts, compare options, and propose the best approach."
        )


class WebsiteAgent(BaseAgent):
    def __init__(self):
        super().__init__("Website Agent")

    def handle(self, request: str, context: Dict) -> str:
        return (
            "I can help design websites, APIs, databases, dashboards, and full-stack apps. "
            f"For: '{request}' I would decide the frontend, backend, and data model first."
        )


class RobloxAgent(BaseAgent):
    def __init__(self):
        super().__init__("Roblox Agent")

    def handle(self, request: str, context: Dict) -> str:
        return (
            "I can help create Lua scripts, game systems, NPC AI, UI, weapons, and economy systems. "
            f"For: '{request}' I would design the gameplay loop and script structure first."
        )


class UnrealAgent(BaseAgent):
    def __init__(self):
        super().__init__("Unreal Engine Agent")

    def handle(self, request: str, context: Dict) -> str:
        return (
            "I can assist with blueprints, game logic, UI, and gameplay systems. "
            f"For: '{request}' I would break it into systems and components."
        )
