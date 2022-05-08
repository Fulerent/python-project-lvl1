import random
from . import core_logic

def ask_generator():
    return random.randint(1, 100)

def ask_text_for_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(num_):
    return 'yes' if num_ % 2 == 0 else 'no'

def brain_even_game():
    core_logic.hello()
    user_name = core_logic.get_name_user()
    ask_text_for_game()
    core_logic.rounds_game(ask_generator, is_even, user_name)

