
# OBJECTS
# IN PYTHON 3 eveyrhing is an object!!!

class Egg:
	# constructor - keyword __init__. self - reference to object it self.
	def __init__(self, kind='fried'):
		self.kind = kind

	def whatKind(self):
		return self.kind

# Class is like a blueprint. 
# Class defines how the object is created.
# Object is an instance of a class.
# Object is an encapsulation of all methods and variables that inside of the class.

def main():
	
	# Create object with default value
	fried = Egg()
	
	# with value
	scrambled = Egg('scrambled')


	print(fried.kind)
	print(scrambled.kind)




if __name__ == '__main__': main()