# SIMPLE OOP

class Fibonacci():

	# ___init___ is contructor of class.
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def series(self):
		while(True):
			yield(self.b)
			self.a, self.b = self.b, self.a + self.b


f = Fibonacci(0, 1)

for r in f.series():
	if r > 100: break
	print(r, end='\n')


# self - is reference to object.
# object - is instance of class.
# instantination - process of creating object.
# class - is like blueprint to object.

