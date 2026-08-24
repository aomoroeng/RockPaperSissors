from random import choice

RPS = ["ROCK", "PAPER", "SISSORS"]


def main():
    user_ = user()
    bot_ = bot()
    print(f"{user_} ---> {bot_}")
    print(logic(user_, bot_))


def user():
    while True:
        user_inpt = input("> ")
        if user_inpt in RPS:
            return user_inpt


def bot():
    return choice(RPS)


def logic(user, bot):
    if user == bot:
        return "tie"
    elif (
        (user == "PAPER" and bot == "ROCK")
        or (user == "SISSORS" and bot == "PAPER")
        or (user == "ROCK" and bot == "SISSORS")
    ):
        return "user won"
    else:
        return "user lost"


if __name__ == "__main__":
    main()
