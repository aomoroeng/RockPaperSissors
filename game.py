from random import choice

RPS = ["ROCK", "PAPER", "SISSORS"]


def main():
    print(user())
    print(bot())


def user():
    while True:
        user_inpt = input("> ")
        if user_inpt in RPS:
            return user_inpt


def bot():
    return choice(RPS)


if __name__ == "__main__":
    main()
