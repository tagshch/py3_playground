
# GENERATOR pattern

'''
def isprime(n):
	if n == 1:
		return False
	for x in range(2,n):
		if n % x == 0:
			return False
		else:
			return True

def primes(n=1):
	while(True):
		if isprime(n): yield n
		n += 1

for n in primes():
	if n > 100: break
	print(n)

'''

# YIELD construction

def func1(n=1):
	for x in range(1,10):
		if x>0: yield x

for n in func1():
	print(n)

