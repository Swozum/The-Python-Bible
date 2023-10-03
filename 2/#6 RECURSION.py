#6 RECURSION
#Recursão e retornar a função alterando algum parametro no final da mesma ate atingiro objetivo final

def function():
	function()
function()

#Factorial Calculation

def factorial(n):
	if n < 1:
		return 1
	else:
		number = n * factorial(n - 1)
		return number