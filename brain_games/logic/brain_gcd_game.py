import random
from .core_logic import start_game

task = 'Find the greatest common divisor of given numbers.'

def ask_generator():
    return "{0} {1}".format(random.randint(1, 100), random.randint(1, 100))


def is_minimal_div(response):
    num1, num2 = int(response.split(" ")[0]), int(response.split(" ")[1])
    div = num1 // 2 if num1 < num2 else num2 // 2

    for n in range(div, 2, -1):
        if num1 % n == 0 and num2 % n == 0:
            return str(n)
    else:
        return str(1)

    
def brain_gcd_game():
    start_game(task, ask_generator, is_minimal_div)

