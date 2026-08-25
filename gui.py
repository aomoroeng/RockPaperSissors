from game import Game
import tkinter as tk

root = tk.Tk()


def center():
    width = 250
    height = 100
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    return f"{width}x{height}+{x}+{y}"


root.geometry(center())
root.title("RPS")
game = Game()
tk.Button(root, text="Rock", command=lambda: play_move("ROCK")).grid(row=0, column=3)


def show_bot_choice(choice):
    tk.Label(root, text=choice).grid(row=0, column=0)


def show_result(result):
    tk.Label(root, text=f"A {result} for you").grid(row=1, column=2)


def play_move(move):
    bot_choice, result = game.play(move)

    show_bot_choice(bot_choice), show_result(result)


root.mainloop()
