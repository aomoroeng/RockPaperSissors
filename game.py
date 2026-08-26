from random import choice

# CONSTANTS
WIN, LOSS, TIE = "WIN", "LOSS", "TIE"
BEATS = {"ROCK": "SCISSORS", "PAPER": "ROCK", "SCISSORS": "PAPER"}
KEYS = {"r": "ROCK", "p": "PAPER", "s": "SCISSORS"}
EMOJI = {"ROCK": "🪨", "PAPER": "📄", "SCISSORS": "✂️"}
RPS = list(BEATS)

if set(KEYS.values()) != set(BEATS):
    raise ValueError(f"BEATS/KEYS mismatch | {set(KEYS.values()) ^ set(BEATS)}")
if set(EMOJI) != set(BEATS):
    raise ValueError(f"EMOJI mismatch | {set(EMOJI) ^ set(BEATS)}")
if set(BEATS.values()) != set(BEATS):
    raise ValueError(f"BEATS values mismatch | {set(BEATS.values()) ^ set(BEATS)}")


def score_line(score):
    return f"W:{score[WIN]} | L:{score[LOSS]} | T:{score[TIE]}"


def show(move):
    return EMOJI[move]


def user(inpt):
    inpt = inpt.strip().upper()
    if inpt in RPS:
        return inpt
    return KEYS.get(inpt.lower())


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
        self.score.update({WIN: 0, LOSS: 0, TIE: 0})
