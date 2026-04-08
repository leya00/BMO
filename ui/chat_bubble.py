import tkinter as tk

class ChatInput:
    def __init__(self, root, x, y, on_submit):
        self.root = root
        self.x = x
        self.y = y
        self.on_submit = on_submit

        self.bmo_window = tk.Toplevel(root)
        self.bmo_window.geometry(f"+{x}+{y}")
        self.bmo_window.wm_attributes("-topmost", True)

        self.bmo_window_entry = tk.Entry(self.bmo_window, font=("Arial", 20))
        self.bmo_window_entry.pack(padx=8, pady=4)
        self.bmo_window_entry.focus_set()
        self.bmo_window_entry.bind("<Return>", self._submit)

        self.bmo_window = tk.Label(self.bmo_window, text="talk to bmo", font=("Arial", 14))
        self.bmo_window.pack(pady=10)
        
    def _submit(self, event=None):
        user_input = self.bmo_window_entry.get().strip()
        self.bmo_window.destroy()
        if user_input:
            self.on_submit(user_input)
        

        