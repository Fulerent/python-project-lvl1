import prompt
import random


def is_even(num_):
	return 'yes' if num_ % 2 == 0 else 'no'
	

def brain_even(name):
	n = 1
	user_name = name

	while n < 4:
		in_random_number = random.randint(1, 100)
		print('Question: {in_random_nubmer}')
		resp_user = prompt.string('Your answer: ')
		
		if is_even(in_random_nubmer) == resp_user:
			print("Correct!")
			n += 1
			
			if n == 3:
				print('Congratulations, {name}')
				break
		else:
			print("{1} is wrong answer ;(. Correct answer was '{2}'".format(is_even(in_random_number), resp_user))
			print('Let\'s try again, {}'.format(user_name))
			break
	
	pass
