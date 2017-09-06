#
# CONDITIONAL STATEMENTS
#

def main():
	x, y = 100, 100

	if(x < y):
		st = "x < y"
	elif(x == y):
		st = "x == y"
	else:
		st = "x > y"

	print(st)

	# Conditional statement let you use "a if CONDITION else b"
	st = "x < y" if (x < y) else "x > y"

	print (st)

	# Optimized
	st = "x < y" if (x < y)  else "x > y"


if __name__ == "__main__":
	main()