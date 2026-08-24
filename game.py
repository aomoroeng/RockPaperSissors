from random import choice

WIN, LOSS, TIE = "WIN", "LOSS", "TIE"
BEATS = {"ROCK": "SCISSORS", "PAPER": "ROCK", "SCISSORS": "PAPER"}
RPS = list(BEATS)


def user(inpt):
    inpt = inpt.strip().upper()
    return inpt if inpt in RPS else None


def bot():
    return choice(RPS)


def logic(user_choice, bot_choice):
    if user_choice == bot_choice:
        return TIE
    return WIN if BEATS[user_choice] == bot_choice else LOSS


class Game:
    def __init__(self):
        self.score = {WIN: 0, LOSS: 0, TIE: 0}

    def play(self, user_choice):
        if user_choice not in RPS:
            raise ValueError("user_choice is not in RPS")
        bot_choice = bot()
        result = logic(user_choice, bot_choice)
        self.score[result] += 1
        return bot_choice, result

    def reset(self):
        self.score = {WIN: 0, LOSS: 0, TIE: 0}
