class Personality:
    """Personality and voice settings for NekoAI."""

    def __init__(self):
        self.voice_options = {
            "male_telugu": "Nice work bro.",
            "female_telugu": "Let’s do this together.",
            "male_english": "Let’s solve this together.",
            "female_english": "You can do it. I’m here with you.",
        }
        self.current_voice = "male_english"

    def voice_message(self, tone: str = "friendly") -> str:
        if tone == "friendly":
            return self.voice_options.get(self.current_voice, "Let’s solve this together.")
        if tone == "motivating":
            return "You can do it. Keep going."
        if tone == "supportive":
            return "I’m with you, and we’ll handle it step by step."
        return "Let’s solve this together."


__all__ = ["Personality"]
