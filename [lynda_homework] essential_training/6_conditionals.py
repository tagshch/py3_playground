# CONDITIONALS

def main():

	# IF-ELSE
	a, b = 0, 1

	if (a > b):
		print('Condition is true')

	elif (a == b):
		print('Condition is true')

	else:
		print('Condition is false')


	# SWITCH
	choices = dict(
		one = "first",
		two = "second",
		three = "third",
		four = "fourth",
		five = "fifth"
	)

	key1 = 'one'
	key2 = 'bingo'

	print('Key exist:', choices.get(key1))
	print('Key non-exist:',choices.get(key2, False))

	# SHORT IF-ELSE
	result = True if a < b else False
	print('Short if-else:', result)



if __name__ == "__main__":	main()
