from __future__ import annotations

from .critic import CriticEngine
from .goal_manager import GoalManager
from .learning import LearningEngine


class NekoAI:
    def __init__(self, owner_name: str = "Owner", memory_path: str = "memory/nekoai_memory.json"):
        self.owner_name = owner_name
        self.memory = MemoryStore(memory_path)
        self.memory.set_owner_name(owner_name)
        self.knowledge = KnowledgeBase()
        self.planner = Planner()
        self.personality = Personality()
        self.goal_manager = GoalManager()
        self.critic = CriticEngine()
        self.learning_engine = LearningEngine(self.memory)
        self.agents = {
            "coding": CodingAgent(),
            "learning": LearningAgent(),
            "research": ResearchAgent(),
            "website": WebsiteAgent(),
            "roblox": RobloxAgent(),
            "unreal": UnrealAgent(),
        }

    def observe(self, request: str) -> str:
        return f"Observed: {request}"

    def understand(self, request: str) -> str:
        matches = self.knowledge.search(request)
        return f"Understanding: {', '.join(matches)}"

    def reason(self, request: str) -> str:
        self.goal_manager.add_goal(self.goal_manager.extract_goal(request))
        return (
            "Reasoning checks: What does the owner want? What is the goal? "
            "What information is missing? What should I do first? What could go wrong? "
            "How can I improve the result?"
        )

    def plan(self, request: str) -> list[str]:
        steps = self.planner.build_plan(request)
        return [f"{step.title}: {step.description}" for step in steps]

    def act(self, request: str) -> str:
        text = request.lower()

        if any(word in text for word in ["code", "python", "javascript", "lua", "script", "bug", "app", "program", "debug"]):
            return self.agents["coding"].handle(request, {"owner": self.owner_name})
        if any(word in text for word in ["study", "learn", "exam", "quiz", "math", "science", "homework", "school"]):
            return self.agents["learning"].handle(request, {"owner": self.owner_name})
        if any(word in text for word in ["research", "compare", "technology", "ai", "ml", "analysis", "report"]):
            return self.agents["research"].handle(request, {"owner": self.owner_name})
        if any(word in text for word in ["website", "web", "api", "frontend", "backend", "dashboard", "full stack"]):
            return self.agents["website"].handle(request, {"owner": self.owner_name})
        if any(word in text for word in ["roblox", "npc", "weapon", "economy", "ui", "lua game"]):
            return self.agents["roblox"].handle(request, {"owner": self.owner_name})
        if any(word in text for word in ["unreal", "blueprint", "level", "gameplay", "ue5", "ue4"]):
            return self.agents["unreal"].handle(request, {"owner": self.owner_name})

        return (
            f"{self.personality.voice_message('friendly')} I can help with coding, learning, research, websites, Roblox, and Unreal Engine. "
            f"Tell me what you want to build or solve."
        )

    def evaluate(self, request: str, plan: list[str], action: str) -> str:
        return self.critic.review(request, plan, action)

    def learn(self, request: str, action: str) -> str:
        return self.learning_engine.record(request, action)

    def remember(self, key: str, value: str) -> None:
        self.memory.remember(key, value)

    def handle_request(self, request: str) -> dict[str, object]:
        observation = self.observe(request)
        understanding = self.understand(request)
        reasoning = self.reason(request)
        plan = self.plan(request)
        action = self.act(request)
        critic = self.evaluate(request, plan, action)
        learning = self.learn(request, action)
        goal_status = self.goal_manager.current_goals()

        return {
            "observation": observation,
            "understanding": understanding,
            "reasoning": reasoning,
            "plan": plan,
            "action": action,
            "critic": critic,
            "learning": learning,
            "goals": goal_status,
        }

    def chat(self, request: str) -> str:
        result = self.handle_request(request)
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

        lines.append(f"- Goal: {result['goals'][-1] if result['goals'] else 'General assistance'}")
        lines.append(f"- Action: {result['action']}")
        lines.append(f"- {result['critic']}")
        lines.append(f"- Learning: {result['learning']}")
        return "\n".join(lines)


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

__all__ = ["NekoAI"]
