#11 FILE OPERATIONS
#Opening And Closing Files
file = open("myfile.txt","r")
file.close()

#Acess Modes
# r   | Reading
# r+  | Reading and Writing
# rb  | Reading Binary File
# rb+ | Reading and Wrinting Binary File
# w   | Writing
# w+  | Reading and Writing(Truncating File)
# wb  | Writing Binary File
# wb+ | Reading and Wrinting Binary File(Truncating File)
# a   | Appending
# a+  | Reading and Appending
# ab  | Appending Binary File
# ab+ | Reading and Appending Binary File

#With Statements
with open("Myfile.txt","r") as file:
	#Some Code here

#Reading From Files
file = open('myfile.txt','r')
print(file.read())
file.close()
# or
with open('myfile.txt', 'r') as file:
	print(file.read())
# or we can specify the quantity of characters with the read()

with open('myfile.txt','r') as file:
	print(file.read(50))

#Writing Into Files
file = open('myfile.txt','w')
print(file.write("Hello File"))
file.flush
file.close()
# OR
with open('myfile.txt', 'w') as file:
	print(file.write("Hello File"))
#Or we can just append
with open('myfile.txt', 'a') as file:
	print(file.write("Hello File"))

#Other Operations
from os import *

#Deleting And Renaming
remove("myfile.txt")
rename("myfile,txt","newfile.txt")
#We can move files to another directory but we cant crate new ones
rename("myfile.txt","newdir/myfile.txt")

#Directory Operations
mkdir("newdir")# make a diretory
chdir("newdir")#change directory
chdir("..")#navigate back to one directory and we can specify like “C:\Users\Python\Desktop\file.txt”
rmdir("newdir")#remove directory