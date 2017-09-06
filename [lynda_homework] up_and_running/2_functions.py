#
# FUNCTIONS
#

# Define function
def func1():
	print("func1 started!")

func1()
print(func1())	# Print none
print(func1)	# Print function

# Function with arguments
def func2(x, y):
	print(x, y)

func2("arg1", "arg2")

# Function that return a value
def func3(x):
	return x*x

print(func3(10))

# Function with default value for an argument
def func4(x, y = 1):
	result = 1
	for i in range(y):
		result = result * x
	return result

print(func4(2), func4(2, 3), func4(y = 3, x = 2)) # NB!

def func5(*args):
	result = 0
	for x in args:
		result = result + x
	return result

print(func5(1, 2, 3, 4))

