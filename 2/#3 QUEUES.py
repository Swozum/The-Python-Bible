#3 QUEUES

import queue

q = queue.Queue()

for x in range(5):
	q.put(x)#Add an element to the queue
for x in range(5):
	print(q.get(x))#Extract an element from the queue
#Commonly know as a FIFO: First In, First Out

#Queuing Resources

import threading
import math

q = queue.Queue()
threads = []

def worker():
	while True:
		item = q.get()
		if item is None:
			break
		print (math.factorial(item))
    q.task_done()
for x in range(5):
	t = threading.Thread(target =worker)
	t.start()
	threads.append(t)
zahlen = [13400,14,5,300,98,88,11,23]

for item in zahlen:
	q.put(item)
q.join()

for i in range(5):
	q.put(None)

#Lifo Queues
q = queue.LifoQueue()
numbers = [1,2,3,4,5]
for x in numers:
	q.put(x)
while not q.empty():
	print(q.get())

#Prioritizing Queues
q = queue.PriorityQueue()
q.put((8,"Some String"))
q.put((1,2023))
q.put((90,True))
q.put((2,10.23))

while not q.empty():
	print(q.get())

q.put((8,"Some String"))
q.put((1,2023))
q.put((90,True))
q.put((2,10.23))

while not q.empty():
	print(q.get()[1])