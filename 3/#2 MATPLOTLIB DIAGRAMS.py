#2 MATPLOTLIB DIAGRAMS
import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(0, 20, 100)
y_values = np.sin(x_values)
#plt.plot(x_values, y_values, )
#plt.show()

x = np.linspace(0, 10, 100)
y = (6* x - 30)** 2
#plt.plot(x, y, )
#plt.show()

#Visualizing Values

numbers = 10*np.random.random(100)
#plt.plot(numbers,'rs')
#plt.show()

#Multiple Graphs

x = np.linspace(0, 5, 200)
y1 = 2 * x
y2 = x ** 2
y3 = np.log(x)
#plt.plot(x,y1)
#plt.plot(x,y2)
#plt.plot(x,y3)
#plt.show()

#Subplots

x = np.linspace(0, 5, 200)
y1 = np.sin(x)
y2 = np.sqrt(x)
plt.subplot(211)
plt.plot(x, y1, 'r-')
plt.subplot(212)
plt.plot(x, y2, 'g--')
plt.show()