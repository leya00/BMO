import os
import json
import ollama
from dotenv import load_dotenv
from config.settings import BMO_SYSTEM_PROMPT, MEMORY_FILE, MAX_HISTORY_TURNS


load_dotenv()

class BMOAgent:
    def __init__(self):
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

    def chat(self, user_message: str, user_name: str = "Friend") -> str:
        system = BMO_SYSTEM_PROMPT.replace("{user_name}", user_name)
        self.history.append({"role": "user", "content": user_message})
        
        response = ollama.chat(
            model="llama3.2",
            messages=[{"role": "system", "content": system}] + self.history[-MAX_HISTORY_TURNS:]
        )
        reply = response['message']['content']
        
        self.history.append({"role": "assistant", "content": reply})
        self._save_history()
        return reply
