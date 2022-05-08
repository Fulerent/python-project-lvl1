from . import start_game
import random

task = 'What is the result of the expression?'

def ask_generator():
    random_sign = ["+", "-", "*"][random.randint(0, 2)]
    one_value = random.randint(1, 100)
    two_value = random.randint(1, 100)

    return "{0} {1} {2}".format(one_value, random_sign, two_value)


def is_correct_result_exp(expression):
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
    start_game(task, ask_generator, is_correct_result_exp)
