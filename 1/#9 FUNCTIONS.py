#9 FUNCTIONS

#Defining Functions
def hello():
	print("Hello")

#Parameters
def print_sum(number1, number2):
	print(number1 + number2)
print_sum(20,30)

#Return Values
def add(number1, number2):
	return number1 + number2
number3 = add(10,30)
print(number3)
print(add(10,30))

#Default Parameters
def say(text='Default Text'):
	print(text)

#Variable Parameters
def sum_of_num(*numbers):
	result = 0
	for x in numbers:
		result += x 
	print(result)
sum_of_num(10,30,20,40)

#Scopes
number = 10
def function():
	global number 
	number += 10
	print(number)