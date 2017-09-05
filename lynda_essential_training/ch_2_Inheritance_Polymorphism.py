# INHERITANCE AND POLYMORPHIZM


# INHERITANCE
class AnimalActions():
	def quack(self): return self.string['quack']
	def feathers(self): return self.string['feathers']
	def bark(self): return self.string['bark']
	def fur(self): return self.string['fur']

class Duck(AnimalActions):
	string = dict(
		quack = 'Quaaaaaak!',
		feathers = 'Gray and white feathers!',
		bark = 'The duck can\'t bark',
		fur = 'The duck has no fur.'
	)

class Person(AnimalActions):
	string = dict(
		quack = 'Person quack',
		feathers = 'Person feathers!',
		bark = 'Person bark',
		fur = 'Person fur.'
	)

class Dog(AnimalActions):
	string = dict(
		quack = 'Dog quack',
		feathers = 'Dog feathers!',
		bark = 'Dog bark',
		fur = 'Dog fur.'
	)

# POLYMORPHISM
# By connections to superclass or by function overloading...
# (load different types of parameter - get different result. But function name same)
# p.s. Method overriding - subclass has same name method as superclass. 
# (Instance of subclass overrides method of superclass.)
# Person ingerit from AnimalActions, so it has functions from AnimalActions.

def in_the_forest(duck):
	print(duck.quack())
	print(duck.feathers())

def in_the_doghouse(dog):
	print(dog.bark())
	print(dog.fur())

def main():
	donald = Duck()
	john = Person()
	fido = Dog()

	print("\nIn the forest:")	
	# o - object in list (which include: donald, john, fido)
	for o in (donald,john,fido):
		in_the_forest(o)

	print("\nIn the doghouse:")
	for o in (donald,john,fido):
		in_the_doghouse(o)

if __name__ == '__main__': main()