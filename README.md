# NekoAI

NekoAI is a fully autonomous AI companion built from scratch. It follows a cognitive loop:

Observe → Understand → Reason → Plan → Act → Evaluate → Learn → Remember

This repository contains the first working starter version of the project: a local Python-based AI companion with memory, planning, and agent-based task handling.

## Features

- Persistent memory system
- Knowledge categories and local lookup
- Goal and task planning
- Specialized agent modules
- Interactive CLI chat loop
- Offline, no external API required

## Project structure

- `main.py` – CLI entry point
- `nekoai/` – core modules for memory, reasoning, planning, and agents

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
python main.py
```

## Example commands

Type any request into the CLI, for example:

- "Help me build a study plan for math and physics"
- "Create a Python script for a quiz app"
- "Plan my weekly coding goals"
- "Research which web stack is best for a simple portfolio site"

## Mission

The long-term goal is to become a loyal digital companion that can:

- help the owner
- learn continuously
- reason and plan
- remember important details
- work without commercial AI APIs

## License

This project is currently under active development.
