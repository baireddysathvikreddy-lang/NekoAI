from typing import Dict, List, Optional

from .agents import (
    CodingAgent,
    LearningAgent,
    ResearchAgent,
    RobloxAgent,
    UnrealAgent,
    WebsiteAgent,
)
from .knowledge import KnowledgeBase
from .memory import MemoryStore
from .planner import Planner


class NekoAI:
    """Core brain for the autonomous AI companion."""

    def __init__(self, memory_path: str = "memory/nekoai_memory.json"):
        self.memory = MemoryStore(memory_path)
        self.knowledge = KnowledgeBase()
        self.planner = Planner()
        self.agents = {
            "coding": CodingAgent(),
            "learning": LearningAgent(),
            "research": ResearchAgent(),
            "website": WebsiteAgent(),
            "roblox": RobloxAgent(),
            "unreal": UnrealAgent(),
        }

    def observe(self, user_request: str) -> str:
        return f"Observed request: {user_request}"

    def understand(self, user_request: str) -> str:
        relevant = self.knowledge.search(user_request)
        return f"Understanding context: {', '.join(relevant)}"

    def reason(self, user_request: str) -> str:
        return (
            "Reasoning questions: What does the owner want? What is the goal? "
            "What information is missing? What should be done first?"
        )

    def plan(self, user_request: str) -> List[str]:
        steps = self.planner.build_plan(user_request)
        return [f"{step.title}: {step.description}" for step in steps]

    def act(self, user_request: str) -> str:
        text = user_request.lower()
        if any(word in text for word in ["code", "python", "javascript", "lua", "bug", "script", "app"]):
            return self.agents["coding"].handle(user_request, {})
        if any(word in text for word in ["study", "learn", "exam", "quiz", "math", "science", "homework"]):
            return self.agents["learning"].handle(user_request, {})
        if any(word in text for word in ["research", "compare", "technology", "ai", "ml", "market"]):
            return self.agents["research"].handle(user_request, {})
        if any(word in text for word in ["website", "api", "dashboard", "frontend", "backend", "full stack"]):
            return self.agents["website"].handle(user_request, {})
        if any(word in text for word in ["roblox", "npc", "weapon", "ui", "game system"]):
            return self.agents["roblox"].handle(user_request, {})
        if any(word in text for word in ["unreal", "blueprint", "level", "gameplay"]):
            return self.agents["unreal"].handle(user_request, {})
        return "I can help with coding, learning, research, websites, Roblox, and game design. Tell me what you want to build."

    def evaluate(self, user_request: str, result: str) -> str:
        return "Evaluation: The response should be helpful, accurate, and aligned with the user goal."

    def learn(self, user_request: str, result: str) -> str:
        self.memory.add_conversation(user_request, result)
        return "Learning update: I have stored this interaction and will improve future responses."

    def remember(self, key: str, value: str) -> None:
        self.memory.remember(key, value)

    def handle_request(self, user_request: str) -> Dict[str, object]:
        observation = self.observe(user_request)
        understanding = self.understand(user_request)
        reasoning = self.reason(user_request)
        plan = self.plan(user_request)
        action = self.act(user_request)
        evaluation = self.evaluate(user_request, action)
        learning = self.learn(user_request, action)

        return {
            "observation": observation,
            "understanding": understanding,
            "reasoning": reasoning,
            "plan": plan,
            "action": action,
            "evaluation": evaluation,
            "learning": learning,
        }

    def chat(self, user_request: str) -> str:
        result = self.handle_request(user_request)
        response = [
            "NekoAI Response",
            f"- {result['observation']}",
            f"- {result['understanding']}",
            f"- {result['reasoning']}",
            "- Plan:",
        ]
        for step in result["plan"]:
            response.append(f"  • {step}")
        response.append(f"- Action: {result['action']}")
        response.append(f"- Evaluation: {result['evaluation']}")
        response.append(f"- Learning: {result['learning']}")
        return "\n".join(response)
