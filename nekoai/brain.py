from __future__ import annotations

from typing import Dict, List

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
from .personality import Personality
from .planner import Planner


class NekoAI:
    """Core autonomous AI companion."""

    def __init__(self, owner_name: str = "Owner", memory_path: str = "memory/nekoai_memory.json"):
        self.owner_name = owner_name
        self.memory = MemoryStore(memory_path)
        self.memory.set_owner_name(owner_name)
        self.knowledge = KnowledgeBase()
        self.planner = Planner()
        self.personality = Personality()
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
        matches = self.knowledge.search(user_request)
        return f"Understanding context: {', '.join(matches)}"

    def reason(self, user_request: str) -> str:
        return (
            "Reasoning checklist: What does the owner want? What is the goal? "
            "What information is missing? What should I do first? What could go wrong?"
        )

    def plan(self, user_request: str) -> List[str]:
        steps = self.planner.build_plan(user_request)
        return [f"{step.title}: {step.description}" for step in steps]

    def act(self, user_request: str) -> str:
        text = user_request.lower()

        if any(word in text for word in ["code", "python", "javascript", "lua", "script", "bug", "app", "program", "debug"]):
            return self.agents["coding"].handle(user_request, {"owner": self.owner_name})
        if any(word in text for word in ["study", "learn", "exam", "quiz", "math", "science", "homework", "school"]):
            return self.agents["learning"].handle(user_request, {"owner": self.owner_name})
        if any(word in text for word in ["research", "compare", "technology", "ai", "ml", "analysis", "report"]):
            return self.agents["research"].handle(user_request, {"owner": self.owner_name})
        if any(word in text for word in ["website", "web", "api", "frontend", "backend", "dashboard", "full stack"]):
            return self.agents["website"].handle(user_request, {"owner": self.owner_name})
        if any(word in text for word in ["roblox", "npc", "weapon", "economy", "ui", "lua game"]):
            return self.agents["roblox"].handle(user_request, {"owner": self.owner_name})
        if any(word in text for word in ["unreal", "blueprint", "level", "gameplay", "ue5", "ue4"]):
            return self.agents["unreal"].handle(user_request, {"owner": self.owner_name})

        return (
            f"{self.personality.voice_message('friendly')} I can help with coding, learning, research, websites, Roblox, and Unreal Engine. "
            f"Tell me what you want to build or solve."
        )

    def evaluate(self, user_request: str, result: str) -> str:
        return (
            "Evaluation: the response should be directly helpful, realistic, and fit the owner goal. "
            "I will refine it if more detail is needed."
        )

    def learn(self, user_request: str, result: str) -> str:
        self.memory.add_conversation(user_request, result)
        return "Learning update stored: this interaction will improve future guidance."

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
        intro = self.personality.voice_message("friendly")

        lines = [
            f"{intro} NekoAI Response",
            f"- {result['observation']}",
            f"- {result['understanding']}",
            f"- {result['reasoning']}",
            "- Plan:",
        ]

        for step in result["plan"]:
            lines.append(f"  • {step}")

        lines.append(f"- Action: {result['action']}")
        lines.append(f"- Evaluation: {result['evaluation']}")
        lines.append(f"- Learning: {result['learning']}")

        return "\n".join(lines)


__all__ = ["NekoAI"]
