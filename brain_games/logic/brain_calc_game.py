from . import core_logic
import random


def ask_generator():
    random_sign = ["+", "-", "*"][random.randint(0, 2)]
    one_value = random.randint(1, 100)
    two_value = random.randint(1, 100)

    return "{0} {1} {2}".format(one_value, random_sign, two_value)

def ask_text_for_game():
    print('What is the result of the expression?')


def is_even(expression):
    exp = expression.split(" ")
    sing = exp[1]
    num1 = int(exp[0])
    num2 = int(exp[2])

    if sing == "+":
        return str(num1 + num2)
    elif sing == "-":
        return str(num1 - num2)
    elif  sing == "*":
        return str(num1 * num2)

    
def brain_calc_game():
    core_logic.hello()
    user_name = core_logic.get_name_user()
    ask_text_for_game()
    core_logic.rounds_game(ask_generator, is_even, user_name)
