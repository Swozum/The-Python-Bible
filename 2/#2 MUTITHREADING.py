#2 MUTITHREADING
import threading

def hello():
	print("Hello World")

t1 = threading.Thread(target =hello)
t1.start()

#Start vs Run
def function1():
	for x in range(1000):
		print("ONE")
def function2():
	for x in range(1000):
		print("TWO")
t1 = threading.Thread(target =function1)
t2 = threading.Thread(target =function2)
#alternam
t1.start()
t2.start()
#Executa um e depois o outro
t1.run()
t2.run()

#Waiting for Threads

def function():
	for x in range(500000):
		print("Hello World")
t1 = threading.Thread(target =function)
t1.start
print("THIS IS THE END")
#Para executar apos a thread, utilize o .join()
t1 = threading.Thread(target =function)
t1.start()
t1.join()
print("This is the End")
#Voce pode temporizar adicionando um numero dentro do join #.join(numero)

#Thread Classes
class MyThread(threading.Thread):
	def __init__(self, message):
		threading.Thread.__init__(self)
		self.message =  message
	def run(self):
		for x in range(100):
			print(self.message)
m1 = MyThread("This is mythread message!")
m1.start()

#Synchronizing Threds
import time

x = 8192
lock = threading.Lock()
#ajuda a utilizar uma mesma variavel em mais de uma thread sem causar problemas

def halve():
	global x,lock
	lock.acquire()
	while (x > 1):
		x /= 2
		print(x)
		time.sleep(1)
	print("END!")
	lock.release()

def double():
	global x, lock
	lock.acquire()
	while(x < 16384):
		x *= 2
		print(x)
		time.sleep(1)
	print("End!")
	lock.release()

t1 = threading.Thread(target =halve)
t2 = threading.Thread(target =double)

t1.start()
t2.start()

#Semaphores

semaphore = threading.BoundedSemaphore(value = 5)
def acess(thread_number):
	print(f"{thread_number}: Trying access...")
	semaphore.acquire()
	print(f"{thread_number}: Access granted!")
	print(f"{thread_number}: Waiting 5 seconds...")
	time.sleep(5)
	semaphore.release()
	print(f"{thread_number}: Realeasing!")
for thread_number in range(10):
	t = threading.Thread(target =acess, args =(thread_number))
	t.start()

#Events
event = threading.Event()

def func():
	print("Waiting for event...")
	event.wait()
	print("Continuing!")
thread = threading.Thread(target =func)
thread.start()

x = input("Trigger event: ")
if(x == "yes"):
	event.set()

#Daemon Threads
path = "text.txt"
text = ""

def readFile():
	global path, text
	while True:
		with open(path) as file:
			text = file.read()
		time.sleep(3)
def printloop():
	global text
	for x in range (30):
		print(text)
		time.sleep(1)
t1 = threading.Thread(target =readFile, daemon = True)
t2 = threading.Thread(target =printloop)
t1.start()
t2.start()