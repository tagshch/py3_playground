#
# LOOPS
#

def main():
	x = 0

	# while loop
	while (x < 5):
		print('while-loop', x)
		x = x + 1

	# for loop
	for x in range(5, 8):
		print('for-loop', x)

	# break loop
	for x in range(8, 18):
		if (x == 15): break
		if (x % 2 == 0): continue
		print('break-loop', x)

	# for loop over collection
	days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
	for d in days:
		print('collection-loop', d)

	# enumerate
	for i, d in enumerate(days):
		print('enumerate', i, d)

if __name__ == "__main__":
	main()
