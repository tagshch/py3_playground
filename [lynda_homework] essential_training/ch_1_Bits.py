a,b = 0,1
print("a less than b." if a < b else "b bigger.")

# FIBONACCI
while b < 50:
	print(b)
	a,b = b, a+b

# fh - FILE HANDLER
fh = open('ch_1_lines.txt')
for line in fh.readlines():
	print(line, end='')

# function
def isprime(n):
	if n == 1:
		print('1 is special')
		return False

	for x in range(2, n):
		if n % x == 0:
			print("{} equals {} x {}".format(n,x,n//x))
			return False
		else:
			print(n, 'is a prime number.')
			return True

for n in range (1,20):
	isprime(n)



