#1 CLASSES AND OBJECTS
#Creating Classes
class Car1:
	def __init__(self,manufacturer, model, hp):
		self.manufacturer = manufacturer
		self.model = model
		self.hp = hp
#Constructor
#__init__

#Addidng Functions
class Car2:
	def __init__(self,manufacturer, model, hp):
		self.manufacturer = manufacturer
		self.model = model
		self.hp = hp

	def print_info(self):
		print(f"Manufacturer: {self.manufacturer}, Model: {self.model}, HP: {self.hp}")

#Class Variables
class Car:

	amount_cars = 0

	def __init__(self, manufacturer, model, hp):
		self.manufacturer = manufacturer
		self.model = model
		self.hp = hp
		Car.amount_cars += 1

	def print_info(self):
		print(f"Manufacturer: {self.manufacturer}, Model: {self.model}, HP: {self.hp}")

	def print_car_amount(self):
		print(f"Amount: {Car.amount_cars}")

#Destructors
class Car3:
	amount_cars = 0

	def __init__(self, manufacturer, model, hp):
		self.manufacturer = manufacturer
		self.model = model
		self.hp = hp
		Car.amount_cars += 1

	def __del__(self):
		print("Object gets deleted!")
		Car.amount_cars -= 1

#Creating Objects
mycar1 = Car("Tesla","Model X", 525)
mycar1.print_info()
mycar1.print_car_amount()

mycar2 = Car("BMW", "X3", 200)
mycar3 = Car("VW","Golf",100)
mycar3.print_info()
print(mycar3.print_car_amount())

#Hidden Attributes
class MyClass:

	def __init__(self):
		self.__hidden = "Hello"
		print(self.__hidden)
m1 = MyClass()

#Inheritance
class Person:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def get_older(self, years):
		self.age += years

class Programmer(Person):

	def __init__(self, name, age, language):
		super(Programmer, self).__init__(name, age)
		self.language = language

	def print_language(self):
		print(f"Favorite Programming Language is {self.language}")

p1 = Programmer("Mike", 30, "Python")
print(p1.name)
print(p1.age)
print(p1.language)
p1.get_older(5)
print(p1.age)

#Overwriting Methods
class Animal:
	def __init__(self, name):
		self.name = name

	def make_sound(self):
		print("Sound!!!")

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)

	def make_sound(self):
		print("Bark!!")

#Operating Overloading
class Vector():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return f"X: {self.x}, Y: {self.y}"
	
	def __add__(self, other):
		return Vector(self.x + other.x,self.y + other.y)

	def __sub__(self, other):
		return Vector(self.x - other.x, self.y - other.y)

v1 = Vector(3, 5)
v2 = Vector(6, 2)
v3 = v1 + v2
v4 = v1 - v2
print(v1)
print(v2)
print(v3)
print(v4)