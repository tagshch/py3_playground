#  USING NUMBERS


def main():
	# Integer type
	num = 42
	print(type(num), num)
	num = 42 // 9
	print(type(num), num)	

	# Float type
	num = 42.0
	print(type(num), num)
	num = 42/9	
	print(type(num), num)
	num = round(42/9, 3)
	print(type(num), num)

	# Remainder (Module)
	num = 42 % 9
	print(type(num), num)

	# Flota to int, etc.
	num = int(42.9)
	mun = float(43)
	print(type(num), type(mun))


if __name__ == '__main__': main()