#
# CLASSES
#

# Define class
class MyClass():
	def method1(self):
		print('myClass.method1')

	def method2(self, x):
		print('myClass.method2', x)


# Inheritance and
class AnotherClass(MyClass):
	def method1(self):
		MyClass.method1(self)
		print('AnotherClass.method1')

	def method2(self, x):
		print('AnotherClass.method2', x)


def main():

	x = MyClass()
	x.method1()
	x.method2('This is an argument!')

	y = AnotherClass()
	y.method2('Another argument!')
	y.method1()



if __name__ == '__main__':
	main()