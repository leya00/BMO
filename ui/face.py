from PIL import Image, ImageTk
import tkinter as tk

class BMOSprite:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas 
        self.frames = []
        self.current_frame = 0

        sprite_sheet = Image.open("assets/sprites/bmo_idle1-sheet.png")
        slice_width = 64
        slice_height = 128
        
        for i in range(3):
            x1 = i * slice_width
            frame = sprite_sheet.crop((x1, 0, x1 + slice_width, slice_height))
            self.frames.append(ImageTk.PhotoImage(frame))

    def animate(self):
        self.canvas.delete("all")
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        frame = self.frames[self.current_frame]
        self.canvas.create_image(0, 0, image=frame, anchor="nw")