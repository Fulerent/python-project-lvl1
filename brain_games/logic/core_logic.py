import prompt


def hello():
	print('Welcome to the Brain Games!')


def get_name_user():
	name = prompt.string('May I have your name? ')
	print('Hello, {}!'.format(name))
	return name


def rounds_game(ask_generator, is_correct_result, name):
    count_win = 0


    while True:
        ask = ask_generator()
        print('Question: {}'.format(ask))
        resp_user = prompt.string('Your answer: ')

        if is_correct_result(ask) == resp_user:
                print("Correct!")
                count_win += 1

                if count_win == 3:
                    print('Congratulations, {}'.format(name))
                    break
        else:

            print('"{0}" is wrong answer ;(. Correct answer was "{1}"'.format(
                resp_user, is_correct_result(ask)))
            print('Let\'s try again, {}!'.format(name))
            break




