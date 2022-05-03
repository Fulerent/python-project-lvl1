from brain_games.logic_brain_even import brain_even
from brain_games.hello import hello, get_user_name

def main():
	print('Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == '__main__':
    hello()
    user_name = get_user_name()
    main()
    brain_even(user_name)
