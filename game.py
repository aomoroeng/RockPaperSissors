from random import choice


def main():
    print(bot())


def bot():
    RPS = ["ROCK", "PAPER", "SISSORS"]
    return choice(RPS)


if __name__ == "__main__":
    main()
