#12 STRING FUNCTIONS
#String As Sequences
text: [str] = "Hello World"
print (text[:5])#will print Hello
print (text[6:11])#will print World
text: [str] = "Hello World"
for x in text:
	print(x)

#Escape Characters
#  \b  | Backspace
#  \n  | New Line
#  \s  | Space
#  \t  | Tab

#String Formatting
 name, age = "John",25
 print("%s is my name!"%name)
 print("I am %d years old!"%age)
 #OR
 print("My name is {} and i am {} years old".format(name, age))
 #OR
 print(f"My name is{name} and i am {age} years old")

#String Functions
#Case Manipulations
string: [str] = "Hello World"
string.lower()#Converts all the letters to lowercase
print(string)
string.upper()#Converts all the letters to uppercase
print(string)
string.title()#Converts all letters to titlecase
print(string)
string.capitalize()#Converts first letter to uppercase
print(string)
string.swapcase()#Swaps the case of all letters
print(string)

#Count Function
text: [str] = "I like you and you like me!"
print(text.count("you"))

#Find Function
text: [str] = "I like you and you like me !"
print(text.find("you"))

#Join Function
names: [list] = ["Mike","John","Anna"]
sep = "-"
print(sep.join(names))

#Replace Function
text: [str] = "I like John and John is my friend!"
text = text.replace("John","Anna")
print(text)

#Split Function
names = "John,Max,Bob,Anna"
name_list = names.split(",")

#Triple Quotes
''' este comente serve para
usar comenterios em diversas
linhas'''