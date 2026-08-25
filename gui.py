from game import Game, RPS, WIN, LOSS, TIE
import tkinter as tk

root = tk.Tk()


def center():
    width = 300
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    return f"{width}x{height}+{x}+{y}"


root.geometry(center())
root.title("RPS")
game = Game()


bot_var = tk.StringVar(value="-")
result_var = tk.StringVar(value="---")
score_var = tk.StringVar()

tk.Label(root, textvariable=bot_var).pack()
tk.Label(root, textvariable=result_var).pack()
tk.Label(root, textvariable=score_var).pack()


def show_score():
    s = game.score
    score_var.set(f"W:{s[WIN]} | L:{s[LOSS]} | T:{s[TIE]}")


def play_move(move):
    bot_choice, result = game.play(move)
    bot_var.set(f"bot: {bot_choice}")
    result_var.set(f"it is a {result}")
    show_score()


for move in RPS:
    tk.Button(root, text=move.title(), command=lambda m=move: play_move(m)).pack()
tk.Button(root, text="Reset", command=lambda: (show_score(), game.reset())).pack()


root.mainloop()
