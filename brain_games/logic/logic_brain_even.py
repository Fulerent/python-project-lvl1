import prompt
import random


def is_even(num_):
	return 'yes' if num_ % 2 == 0 else 'no'
	

def brain_even(user_name):
	n = 0

	while True:
		in_random_number = random.randint(1, 100)
		print('Question: {}'.format(in_random_number))
		resp_user = prompt.string('Your answer: ')
		
		if is_even(in_random_number) == resp_user:
			print("Correct!")
			n += 1
			
			if n == 3:
				print('Congratulations, {}'.format(user_name))
				break
		else:
			print("{0} is wrong answer ;(. Correct answer was '{1}'".format(is_even(in_random_number), resp_user))
			print('Let\'s try again, {}'.format(user_name))
			break
	
	pass
