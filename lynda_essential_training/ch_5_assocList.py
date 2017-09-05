# ASSOCIATIVE DICTIONARY (HASH)

def main():
	# define dictionary
	d = {'one':1,'two':2,'three':3,'four':4 }

	# UNSORTED
	for k in d:
		print(k, d[k])

	# SORTED by key (alphabetical!!!)
	for k in sorted(d.keys()):
		print(k, d[k])

	print()

	# better DEFINE
	d2 = dict(
		one = 1, two = 2, three = 3, four = 4, five = '5 val'
	)
	d2['six'] = 6

	for k in d2:
		print(k, d2[k])

if __name__ == '__main__':main()