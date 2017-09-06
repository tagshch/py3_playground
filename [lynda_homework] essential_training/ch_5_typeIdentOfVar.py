#  Type and Id of variable

# In python everythin is object. Object has ID.
# ID - unique number. Important in work with immutable objects.

# x - is an object
x = 42
print(id(x))
print(type(x))

# y - is the same object to x
y = 42
print(id(y)) 
# Check if its same
print(x == y)
print(x is y)


# ANOTHER EXAMPLE
x = dict(x = 42)
print(type(x))
print(x)
print(id(x))

y = dict(x = 42)
print(id(y))
# NOT SAME - because dictionaries are IMMUTABLE!!!

# Check if - x equals y / if x is y.
print(x == y)
print(x is y) # get false, because the are different objects!
# 
# IS operator used to check if 2 different variables reference to the same object.
# 

