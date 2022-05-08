from .core_logic import start_game
import random

task = 'What is the result of the expression?'

def logic():
    random_sign = ["+", "-", "*"][random.randint(0, 2)]
    one_value = random.randint(1, 100)
    two_value = random.randint(1, 100)
    result_print = "{0} {1} {2}".format(one_value, random_sign, two_value)

    return result_print, is_correct_result_exp(one_value, random_sign, two_value)


def is_correct_result_exp(num1, sing, num2):
    if sing == "+":
        return str(num1 + num2)
    elif sing == "-":
        return str(num1 - num2)
    elif  sing == "*":
        return str(num1 * num2)

    
def brain_calc_game():
    start_game(task, logic)
