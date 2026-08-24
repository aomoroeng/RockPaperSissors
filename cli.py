from game import user, Game

def main():
    game = Game()
    while True:
        try:
            user_choice = user(input("> "))
        except (EOFError, KeyboardInterrupt):
            return
        if user_choice is None:
            print("Pick ROCK, PAPER or SCISSORS")
            continue
        bot_choice, result = game.play(user_choice)
        print(f"{user_choice} ---> {bot_choice}: {result}")
        print(game.score)


if __name__ == "__main__":
    main()
