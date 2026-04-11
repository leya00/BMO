from email.mime import message
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
import threading
from ui.face import BMOSprite
from ui.chat_bubble import ChatInput
from config import settings
from core.agent import BMOAgent

class BMOWindow:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.geometry(f"{settings.WINDOW_WIDTH}x{settings.WINDOW_HEIGHT}")
        self.root.overrideredirect(True)
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-transparentcolor", "white")

        self.bmo_canvas = tk.Canvas(self.root, width=settings.WINDOW_WIDTH, height=settings.WINDOW_HEIGHT, bg="white", highlightthickness=0)
        self.bmo_canvas.pack()

        self.bmo_sprite = BMOSprite(self.bmo_canvas)
        self.animate()

        self._set_position()

        self.agent = BMOAgent()

        self.bmo_canvas.bind("<Button-1>", self.on_click)
        
        self.bubble = None
        self.bubble_label = None

        self.user_name = self._load_user_name()

        self._boot_sequence()

    def animate(self):
        self.bmo_sprite.animate()
        self.root.after(200, self.animate)

    def _set_position(self):
        sh = self.root.winfo_screenheight()
        x = 10
        y = sh - settings.WINDOW_HEIGHT - 18  
        self.root.geometry(f"+{x}+{y}")

    def on_click(self, event):
        x = self.root.winfo_x()
        y = self.root.winfo_y() - 80
        ChatInput(self.root, x, y, self.handle_user_input, auto_close=False)

    def handle_user_input(self, message:str):
        threading.Thread(target=self._ask_bmo, args=(message,), daemon=True).start()
    
    def _ask_bmo(self, message: str):
        name = getattr(self, "user_name", "friend")
        reply = self.agent.chat(message, user_name=name)
        self.root.after(0, lambda: self._show_reply(reply))

    def _show_reply(self, reply: str):

        if not self.bubble or not self.bubble.winfo_exists():
            self.bubble = tk.Toplevel(self.root)
            self.bubble.overrideredirect(True)
            self.bubble.wm_attributes("-topmost", True)
            self.bubble.geometry(f"+{self.root.winfo_x()}+{self.root.winfo_y() - 80}")

            self.bubble_label = tk.Label(
                self.bubble,
                text="",
                font=("Arial", 10),
                bg="#b2e6dd",
                wraplength=200,
                padx=10,
                pady=8
            )
            self.bubble_label.pack()

        self.bubble_label.config(text=reply)

    def _boot_sequence(self):
        self.root.after(1000, lambda: self._show_reply("Finn, Jake, where are you?! I am in a computer!"))
        self.root.after(5000, lambda: self._show_reply("You are not Finn... more friends! More friends to go around!"))
        if self.user_name == "friend":
            self.root.after(9000, lambda: self._show_reply("What is your name?"))
            self.root.after(12000, self._ask_name)
        else:
            self.root.after(9000, lambda: self._show_reply(f"Hello {self.user_name}! I missed you."))

    def _ask_name(self):
        x = self.root.winfo_x()
        y = self.root.winfo_y() - 80
        ChatInput(self.root, x, y, self._save_name, auto_close=True)

    def _save_name(self, name: str):
        self.user_name = name
        import json
        with open("memory/user.json", "w") as f:
            json.dump({"name": name}, f)
        self._show_reply(f"Hello {name}! I am BMO.")

    def _load_user_name(self) -> str:
        try:
            import json
            with open("memory/user.json", "r") as f:
                return json.load(f)["name"]
        except:
            return "friend"
