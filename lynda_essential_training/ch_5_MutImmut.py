# MUTABLE AND IMMUTABLE OBJECTS

# Every object in Python is an object.
# - variables, functions, even code

# Every object has an ID, type and value
# - ID uniquely identifies a particular instance of an object.
#	- cannot change for the life of the project.
# - Type identifies the class of an object.
# 	- cannot change for the life of the object.
# - Value is the contents of the object.
# 	- mutable objects can change value, immutable objects cannot.


x = 42
print()
print(id(x))
print(type(x))

# All variables in Python are first class objects
#  	- what looks like a simple variable are more complex.

# MUTABLE and IMMUTABLE objects
# Mutable objects may change value, immutable objects may not.
# 	- may look like it's value changes
# 	- distinction is visible using id()
# 	- container objects(tuples, lists, etc.) may appear to change value

y = 45
print()
print(y)
print(type(y))
print(id(y))
y = 48
print(id(y))

# Most fundamental types in Python are immutable:
# 	- numbers, strings, tuples.
# Mutable objects include:
# 	- lists, dictionaries, other objects depending upon implementation.





