def main():
	# Tuple (immutable)
	x = (1,2,3)
	print(type(x),x)
	# List (mutable)
	y = [1,2,3]
	y.append(5)
	y.insert(2,7)
	print(type(y),y)

	# String (immutable)
	z = 'string'
	print(type(z),z[2:4])
	for i in z:
		print(i)



if __name__ == '__main__': main()