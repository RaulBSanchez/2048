import _tkinter as tk

class Game(tk.Frame):
    def __init__(self):
        tk.Frame._init_(self)
        self.grid()
        self.master.title("2048")


        self.main_grid = tk.Frame(
            self, b
        )