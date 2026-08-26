from game import Game, RPS, KEYS, score_line, show
import tkinter as tk
from tkinter import ttk

# CONSTANTS
BG = "black"
FG = "white"


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


def center(root, width=500, height=200):
    x = (root.winfo_screenwidth() - width) // 2
    y = (root.winfo_screenheight() - height) // 2
    return f"{width}x{height}+{x}+{y}"


class App:
    def __init__(self, root):
        self.root = root

        # set grid
        self.root.columnconfigure((0, 1, 2), weight=1)
        self.root.rowconfigure((0, 1), weight=1)

        # set frames
        self.bot_frame = tk.Frame(self.root, bg=BG, padx=30, pady=30)
        self.bot_frame.grid(row=0, column=0)

        self.user_frame = tk.Frame(self.root, bg=BG, padx=30, pady=30)
        self.user_frame.grid(row=0, column=2)

        self.score_frame = tk.Frame(self.root, bg=BG, padx=30, pady=30)
        self.score_frame.grid(row=0, column=1)

        self.root.geometry(center(self.root))
        self.root.configure(bg=BG)
        self.root.title("RockPaperScissors")

        self.game = Game()

        # set stringvars
        self.bot_var = tk.StringVar(value="-")
        self.result_var = tk.StringVar(value="---")
        self.score_var = tk.StringVar()

        for key, move in KEYS.items():
            handler = lambda e, m=move: self.play_move(m)
            self.root.bind(f"<{key}>", handler)
            self.root.bind(f"<{key.upper()}>", handler)

        for move in RPS:
            tk.Button(
                self.user_frame,
                text=show(move),
                command=lambda m=move: self.play_move(m),
            ).grid()

        tk.Button(self.root, text="Reset", command=self.reset).grid(row=1, column=1)

        tk.Label(self.bot_frame, textvariable=self.bot_var, bg=BG, fg=FG).grid()
        tk.Label(self.score_frame, textvariable=self.result_var, bg=BG, fg=FG).grid()
        tk.Label(self.score_frame, textvariable=self.score_var, bg=BG, fg=FG).grid()
        self.show_score()

    def show_score(self):
        self.score_var.set(score_line(self.game.score))

    def play_move(self, move):
        bot_choice, result = self.game.play(move)
        self.bot_var.set(f"bot: {show(bot_choice)}")
        self.result_var.set(result)
        self.show_score()

    def reset(self):
        self.game.reset()
        self.bot_var.set("-----")
        self.result_var.set("---")
        self.show_score()


if __name__ == "__main__":
    main()
