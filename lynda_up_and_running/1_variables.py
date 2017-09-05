#
# VARIABLES
#

# Declare
x = 10
print(x)

# Redeclare
x = "abc"
print(x)

# Error: different types cannot be combined
try:
	print("text" + 123)
except:
	print("Error: Python is strict type language!\n")

# Global vs Local
def renameLocal():
	# global a
	x = "x is renamed locally"
	print(x)

def renameGlobal():
	global x
	x = "x is renamed globally"
	print(x)

renameLocal()
print(x)
renameGlobal()

# Delete variable
del x
try:
	print(x)
except:
	print("\nError: x is already deleted!\n")