import os
import json
import anthropic
from config.settings import ANTHROPIC_API_KEY, BMO_SYSTEM_PROMPT, MEMORY_FILE, MAX_HISTORY_TURNS

class BMOAgent:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        self.history = self._load_history()

    def _load_history(self):
        try:
            with open(MEMORY_FILE, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _save_history(self):
        with open(MEMORY_FILE, "w") as f:
            json.dump(self.history, f, indent=4)

    def chat(self, user_message: str) -> str:
        self.history.append({"role": "user", "content": user_message})
        
        response = self.client.messages.create(
            model="claude-3-5-sonnet-20240620", 
            max_tokens=200,
            system=BMO_SYSTEM_PROMPT,
            messages=self.history[-MAX_HISTORY_TURNS:]
        )
        reply = response.content[0].text if hasattr(response.content[0], 'text') else str(response.content[0])
        
        self.history.append({"role": "assistant", "content": reply})
        self._save_history()
        return reply
