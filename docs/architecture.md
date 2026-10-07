from .memory import MemoryStore
from .knowledge import KnowledgeBase
from .planner import Planner
from .agents import (
    CodingAgent,
    LearningAgent,
    ResearchAgent,
    WebsiteAgent,
    RobloxAgent,
    UnrealAgent,
)


class NekoAI:
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

    def think(self, request: str):
        relevant_areas = self.knowledge.search(request)
        plan = self.planner.build_plan(request)

        if any(word in request.lower() for word in ["code", "python", "javascript", "lua", "app", "script", "bug"]):
            action = self.agents["coding"].handle(request, {})
        elif any(word in request.lower() for word in ["study", "learn", "exam", "math", "science", "quiz", "homework"]):
            action = self.agents["learning"].handle(request, {})
        elif any(word in request.lower() for word in ["research", "compare", "ai", "technology", "ml"]):
            action = self.agents["research"].handle(request, {})
        elif any(word in request.lower() for word in ["website", "api", "backend", "frontend", "dashboard"]):
            action = self.agents["website"].handle(request, {})
        elif any(word in request.lower() for word in ["roblox", "npc", "weapon", "game system", "ui"]):
            action = self.agents["roblox"].handle(request, {})
        elif any(word in request.lower() for word in ["unreal", "blueprint", "gameplay", "level"]):
            action = self.agents["unreal"].handle(request, {})
        else:
            action = "I can help with coding, learning, research, websites, Roblox, Unreal Engine, and game design."

        return {
            "knowledge": relevant_areas,
            "plan": [f"{step.title}: {step.description}" for step in plan],
            "action": action,
        }

    def chat(self, request: str) -> str:
        thought = self.think(request)
        self.memory.add_conversation(request, thought["action"])

        lines = [
            "NekoAI Response",
            f"Knowledge areas: {', '.join(thought['knowledge'])}",
            "Plan:",
        ]

        for step in thought["plan"]:
            lines.append(f"  • {step}")

        lines.append(f"Action: {thought['action']}")
        return "\n".join(lines)


__all__ = ["NekoAI"]
