from game import Game, RPS, KEYS, score_line, show
import tkinter as tk
from tkinter import ttk

# CONSTANTS
BG = "black"
FG = "white"


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


def center(root, width=700, height=300):
    x = (root.winfo_screenwidth() - width) // 2
    y = (root.winfo_screenheight() - height) // 2
    return f"{width}x{height}+{x}+{y}"


class App:
    def __init__(self, root):
        self.root = root

        # grid
        self.root.columnconfigure((0, 1, 2), weight=1, uniform="col")
        self.root.rowconfigure((0, 1), weight=1)

        # frames
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

        # stringvars
        self.bot_var = tk.StringVar(value="bot:  -  ")
        self.result_var = tk.StringVar(value="---")
        self.score_var = tk.StringVar()

        # key_controls
        for key, move in KEYS.items():
            handler = lambda e, m=move: self.play_move(m)
            self.root.bind(f"<{key}>", handler)
            self.root.bind(f"<{key.upper()}>", handler)

        # user_buttons
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure(
            "RPS.TButton",
            background=BG,
            foreground=FG,
            borderwidth=0,
            width=4,
            focuscolor=BG,
        )
        self.style.map(
            "RPS.TButton",
            background=[("active", "#1C1C1C")],
            foreground=[("active", FG)],
        )
        for move in RPS:
            ttk.Button(
                self.user_frame,
                text=show(move),
                command=lambda m=move: self.play_move(m),
                style="RPS.TButton",
            ).grid(pady=5)

        # reset_buttons
        ttk.Button(
            self.root, text="Reset", command=self.reset, style="RPS.TButton"
        ).grid(row=1, column=1)

        # labels
        tk.Label(
            self.bot_frame,
            textvariable=self.bot_var,
            bg=BG,
            fg=FG,
            width=12,
            anchor="center",
        ).grid()
        tk.Label(
            self.score_frame,
            textvariable=self.result_var,
            bg=BG,
            fg=FG,
            width=12,
            anchor="center",
        ).grid()
        tk.Label(
            self.score_frame,
            textvariable=self.score_var,
            bg=BG,
            fg=FG,
            width=16,
            anchor="center",
            font=("Menlo", 13),
        ).grid()
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
        self.bot_var.set("bot:  -  ")
        self.result_var.set("---")
        self.show_score()


if __name__ == "__main__":
    main()
