import tkinter as tk
import threading
from ui.face import BMOSprite
from config import settings

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

    def animate(self):
        self.bmo_sprite.animate()
        self.root.after(200, self.animate)
