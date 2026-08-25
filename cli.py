from game import user, Game, score_line


def main():
    game = Game()
    while True:
        try:
            user_choice = user(input("> "))
        except (EOFError, KeyboardInterrupt):
            return
        if user_choice is None:
            print("Pick ROCK, PAPER or SCISSORS | (r,p,s) | ^c to quit")
            continue
        bot_choice, result = game.play(user_choice)
        print(f"{user_choice} ---> {bot_choice}: {result}")
        print(score_line(game.score))


if __name__ == "__main__":
    main()
