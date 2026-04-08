import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
import threading
from ui.face import BMOSprite
from config import settings
import pystray
from PIL import Image, ImageTk
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

    def animate(self):
        self.bmo_sprite.animate()
        self.root.after(200, self.animate)

    def _set_position(self):
        sh = self.root.winfo_screenheight()
        x = 10
        y = sh - settings.WINDOW_HEIGHT - 18  
        self.root.geometry(f"+{x}+{y}")

    def on_click(self, event):
        print("BMO clicked!")
