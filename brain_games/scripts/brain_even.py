#!/usr/bin/env python
from brain_games.logic.logic_brain_even import brain_even
from brain_games.logic.hello import hello, get_name_user

def main():
	print('Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == '__main__':
    hello()
    user_name = get_name_user()
    main()
    brain_even(user_name)