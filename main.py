#!/usr/bin/env python3

from nekoai.brain import NekoAI


def main() -> None:
    print("NekoAI is starting...")
    print("Type 'exit' to quit. Available examples: study plan, coding task, research, website idea, Roblox project")
    print()

    assistant = NekoAI(owner_name="Owner")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        if user_input.lower() in {"exit", "quit", "bye", "goodbye"}:
            print("NekoAI: Goodbye. See you next time.")
            break

        response = assistant.chat(user_input)
        print("\n" + response)
        print("\n")


if __name__ == "__main__":
    main()
