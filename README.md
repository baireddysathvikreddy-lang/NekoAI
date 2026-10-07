# NekoAI - Autonomous AI Companion

NekoAI is a fully autonomous AI companion built from scratch to help you with coding, learning, research, game development, and more.

## Mission

Create an AI that can:
- Think and reason
- Plan and execute
- Learn from experience
- Remember important things
- Help you achieve your goals
- Work completely offline

## Features

✅ **Autonomous Reasoning Loop**: Observe → Understand → Reason → Plan → Act → Evaluate → Learn → Remember
✅ **Memory System**: Persistent local storage of conversations, goals, and learning
✅ **Multi-Agent Architecture**: Specialized agents for coding, learning, research, websites, Roblox, and Unreal Engine
✅ **Goal Manager**: Track and prioritize your objectives
✅ **Critic Engine**: Evaluate solutions for quality and alignment
✅ **Learning Engine**: Improve responses based on interaction history
✅ **Personality System**: Friendly, motivating, and supportive voice
✅ **No External APIs**: Works completely locally

## Supported Domains

- **Coding**: Python, JavaScript, TypeScript, Lua, C#, Java, Go, Rust
- **Learning**: Study plans, quizzes, worksheets, exam prep
- **Research**: Technology comparison, market analysis, data summaries
- **Websites**: Full-stack web apps, APIs, dashboards, databases
- **Roblox**: Lua scripting, game systems, NPC AI, weapons, UI, economy
- **Unreal Engine**: Blueprints, gameplay logic, level design

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
python main.py
```

## Example Prompts

**Roblox Game Development**:
- "Build me a Roblox game foundation"
- "Create an NPC AI system for my game"
- "Design a weapon system"
- "Build an economy system"
- "Create UI elements for my game"

**Coding**:
- "Generate a Python script for X"
- "Fix this bug in my code"
- "Explain how recursion works"
- "Review my project structure"

**Learning**:
- "Create a study plan for calculus"
- "Make me a quiz on biology"
- "Explain quantum mechanics simply"
- "Build an exam prep schedule"

**Research**:
- "Compare React vs Vue for my project"
- "Analyze Python vs Java for backend"
- "Research best practices for APIs"

**Web Development**:
- "Design a full-stack portfolio website"
- "Build a REST API structure"
- "Plan a dashboard database schema"

## Architecture

NekoAI consists of these core modules:

- **Brain** (`nekoai/__init__.py`): Core cognitive loop and request handling
- **Memory** (`nekoai/memory.py`): Persistent JSON-based storage
- **Knowledge** (`nekoai/knowledge.py`): Local knowledge base and topic matching
- **Planner** (`nekoai/planner.py`): Creates structured plans based on intent
- **Agents** (`nekoai/agents.py`): Specialized task handlers
- **Goal Manager** (`nekoai/goal_manager.py`): Tracks owner objectives
- **Critic** (`nekoai/critic.py`): Evaluates solution quality
- **Learning** (`nekoai/learning.py`): Stores lessons for improvement
- **Personality** (`nekoai/personality.py`): Voice and tone settings

## Long-Term Vision

NekoAI is designed to evolve into:

- A desktop assistant with file/project management
- A web dashboard for organizing work
- Voice interaction with avatar animation
- Stronger long-term memory and learning
- Integration with development tools
- Autonomous task automation
- Real-time collaboration features

## License

This project is under active development and is open for contributions.
