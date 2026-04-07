import tkinter as tk
from ui.window import BMOWindow

def main():
    root = tk.Tk()
    app = BMOWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()