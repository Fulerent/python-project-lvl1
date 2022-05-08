import prompt


def _hello():
	print('Welcome to the Brain Games!')


def _get_name_user():
	name = prompt.string('May I have your name? ')
	print('Hello, {}!'.format(name))
	return name


def _rounds_game(ask_generator, is_true, name):
    count_win = 0


    while True:
        ask = ask_generator()
        print('Question: {}'.format(ask))
        resp_user = prompt.string('Your answer: ')

        if is_true(ask) == resp_user:
                print("Correct!")
                count_win += 1

                if count_win == 3:
                    print('Congratulations, {}'.format(name))
                    break
        else:

            print('"{0}" is wrong answer ;(. Correct answer was "{1}"'.format(
                resp_user, is_true(ask)))
            print('Let\'s try again, {}!'.format(name))
            break


def start_game(task, generator, validate):
    _hello()
    user_name = _get_name_user()
    print(task)
    _rounds_game(generator, validate, user_name)




