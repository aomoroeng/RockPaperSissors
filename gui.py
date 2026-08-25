from game import Game, RPS, KEYS, score_line
import tkinter as tk


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


def center(root, width=200, height=200):
    x = (root.winfo_screenwidth() - width) // 2
    y = (root.winfo_screenheight() - height) // 2
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
            handler =  lambda e, m=move: self.play_move(m)
            self.root.bind(f"<{key}>", handler)
            self.root.bind(f"<{key.upper()}>", handler)


        for move in RPS:
            tk.Button(
                self.root, text=move.title(), command=lambda m=move: self.play_move(m)
            ).pack()
        tk.Button(
            self.root,
            text="Reset",
            command=lambda: (self.game.reset(), self.show_score()),
        ).pack()

        tk.Label(self.root, textvariable=self.bot_var).pack()
        tk.Label(self.root, textvariable=self.result_var).pack()
        tk.Label(self.root, textvariable=self.score_var).pack()
        self.show_score()

    def show_score(self):
        self.score_var.set(score_line(self.game.score))

    def play_move(self, move):
        bot_choice, result = self.game.play(move)
        self.bot_var.set(f"bot: {bot_choice}")
        self.result_var.set(f"it is a {result}")
        self.show_score()


if __name__ == "__main__":
    main()
