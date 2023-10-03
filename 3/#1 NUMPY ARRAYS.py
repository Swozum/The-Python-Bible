#1 NUMPY ARRAYS
import numpy as np
'''
#Creating Arrays
a = np.array([10, 20, 30])
b = np.array([1, 77, 2, 3])

print(a[0])
print(b[2])

#Multi-dimensional  Arrays
a = np.array([
	[10, 20, 30],
	[40, 50, 60]
	])
print(a)

print(a[1][2])

aBigger = np.array([
		[
			[10, 20, 30, 40], [8, 8, 2, 1], [1, 1, 1, 2]
		],
		[
			[9, 9, 2, 39], [1, 2, 3, 3], [0, 0, 3, 2]
		],
		[
			[12, 33, 22, 1], [22, 1, 22, 2], [0, 2, 3, 1]
		]
	], dtype = float)
print(aBigger)

#Full Function
c = np.full((3, 5, 4), 7)
print(c)

#Zeros and Ones
d = np.zeros((3,3))
e = np.ones((2, 3, 4, 2))

print(d)
print(e)

#Empty and Random
a = np.empty((4, 4))
b = np.random.random((2, 3))

print(a)
print(b)
'''
#Ranges

a = np.arange(10, 50, 5)

print(a)

b = np.linspace(0, 100, 11)

print(b)

#NaN
'''
a place holder to indentify that a value is not a number

'''

#Atributes of Arrays
a = np.array([[3,3],["rio",True]])
print(a.shape)#Return the shape of the array
print(a.ndim)#Return the number of dimensios the array have
print(a.size)#Returns the amount of elements in the array
print(a.dtype)#Returns the data type of the values in the array


#Mathematical Operations

a = np.array([
		[1, 4, 2],
		[8, 8, 2]
	])
print(a+2)
print(a-2)
print(a*2)
print(a/2)

b = np.array([
		[1, 2, 3]
	])

c = np.array([
		[1],
		[2]
	])

d = np.array([
		[1, 2, 3],
		[3, 2, 1]
	])
#if there isn't a reasonable way of doing the operations the console will emit a ValueError

#Matematical Functions
print(np.exp(a))#takes e to the power of every element
print(np.sin(a))#Returns the sine of each value
print(np.cos(a))#Returns the cosine of each value
print(np.tan(a))#Returns the tangent of each value
print(np.log(a))#Returns the logarithm of each value
print(np.sqrt(a))#Returns the square root of each value

#Aggregate Functions
print(a.sum())#Returns the sum of all the elements in the array
print(a.min())#Returns the lowest value of the array
print(a.max())#Returns the highest value of the array
print(a.mean())#Returns the arithmetic mean of all values in the array
print(np.median(a))#Returns the median value of the array
print(np.std(a))#Returns the standard deviation of the values in the array


#Manipulatin Arrays

a = np.array([
		[4, 2, 9],
		[8, 3, 2]
	])

a[1][2] = 7
print(a)
#Shape Manipulation Functions
print(a.reshape(3,2))#Returns an array with same values structured in a different shape
print(a.flatten())#Returns a flattened one-dimensional copy
print(a.ravel())#Does the same as flatten but with the actual array
print(a.transpose())#Returns an array with the same values but swapped dimensions
print(a.swapaxes(0,1))#Returns an array with the same values but two swapped axes
for x in a.flat:#Not a function but an iterator for the flattened version of the array
	print(x)
print(a.flat[5])

#Joining Functions
'''///////'''
#Splitting Functions
'''///////'''

print(np.resize(a,(5,4)))
print(np.append(a,[3,4,5,6,7,8,10]))
print(np.insert(a, 1, 1))
print(np.delete(a, 1, 0))

#Loading and saving Arrays
#Numpy Format
a = np.array([
		[10, 20, 30],
		[40, 50, 60],
		[70, 80, 90],
		[100, 110, 120]
	])
np.save('myarray.npy', a)

t = np.load('myarray.npy')
print(t)

#CSV Format

np.savetxt('myarray.csv', a)

h = np.loadtxt('myarray.csv')

print(h)

