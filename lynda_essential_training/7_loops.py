# LOOPS

def main():

	# While-loop (simple fibonacci)
	a, b = 0, 1
	print('While-loop:')
	while b < 50:
		a, b = b, a + b
		print(b, end=' ')


	# For-loop
	print('\nFor-loop:')
	for i in [1,2,3,4]:
		print(i, end=' ')

	print('\nFor-loop:')
	for c in 'foo':
		print(c, end=' ')

	# Enumerate
	print('\nEnumerate:')
	for index, value in enumerate([1,2,3,4]):
		print('index:',index, 'value:',value, end='\n')

	# Break
	for i in [1,2,3]:
		if(i == 1): continue
		print('Break:', i)
		break




if __name__ == "__main__":	main()