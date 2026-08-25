from game import Game, RPS, WIN, LOSS, TIE, KEYS
import tkinter as tk


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


def center(root, width=300, height=200):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    return f"{width}x{height}+{x}+{y}"


class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry(center(self.root))
        self.root.title("RockPaperScissors")
        self.game = Game()
        self.bot_var = tk.StringVar(value="-")
        self.result_var = tk.StringVar(value="---")
        self.score_var = tk.StringVar()
        for key, move in KEYS.items():
            self.root.bind(f"<{key}>", lambda e, m=move: self.play_move(f"{m}"))
        tk.Label(self.root, textvariable=self.bot_var).pack()
        tk.Label(self.root, textvariable=self.result_var).pack()
        tk.Label(self.root, textvariable=self.score_var).pack()

        for move in RPS:
            tk.Button(
                self.root, text=move.title(), command=lambda m=move: self.play_move(m)
            ).pack()
        tk.Button(
            self.root,
            text="Reset",
            command=lambda: (self.game.reset(), self.show_score()),
        ).pack()
        self.show_score()

    def show_score(self):
        s = self.game.score
        self.score_var.set(f"W:{s[WIN]} | L:{s[LOSS]} | T:{s[TIE]}")

    def play_move(self, move):
        bot_choice, result = self.game.play(move)
        self.bot_var.set(f"bot: {bot_choice}")
        self.result_var.set(f"it is a {result}")
        self.show_score()


if __name__ == "__main__":
    main()
