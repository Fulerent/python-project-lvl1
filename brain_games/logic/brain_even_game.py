import random
from . import start_game

ask_text_for_game = 'Answer "yes" if the number is even, otherwise answer "no".'
def ask_generator():
    return random.randint(1, 100)

def is_even(num_):
    return 'yes' if num_ % 2 == 0 else 'no'

def brain_even_game():
    start_game(ask_text_for_game, ask_generator, is_even)

