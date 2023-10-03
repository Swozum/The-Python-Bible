#10 EXCEPTION HANDLING
#Try Except
try:
	print(10 / 0)
	text = "Hello"
	number = int(text)
except ValueError:
	print("Code for ValueError")
except ZeroDivisionError:
	print("Code for ZDE")
except:
	print("Codde for another exceptions")

#Else Statements
try:
	print(10/0)
except:
	print('Error!')
else:
	print('Everything OK!')

#Finally Statements
try:
	print(10/0)
except:
	print('Error')
finally:
	print("Always executed!")