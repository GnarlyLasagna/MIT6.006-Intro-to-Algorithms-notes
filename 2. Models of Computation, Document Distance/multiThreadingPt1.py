import threading

x = 0

def increment():
	"""
	function to increment global variable x
	"""
	global x
	x += 1

def thread_task():
	"""
	task for thread
	calls increment function 100000 times.
	"""
	for _ in range(100000):
		increment()

def main_task():
	global x
	x = 0

	t1 = threading.Thread(target=thread_task)
	t2 = threading.Thread(target=thread_task)

	t1.start()
	t2.start()

	t1.join()
	t2.join()

if __name__ == "__main__":
	for i in range(10):
		main_task()
		print("Iteration {0}: x = {1}".format(i,x))
#Iteration 0: x = 175005
#Iteration 1: x = 200000
#Iteration 2: x = 200000
#Iteration 3: x = 169432
#Iteration 4: x = 153316
#Iteration 5: x = 200000
#Iteration 6: x = 167322
#Iteration 7: x = 200000
#Iteration 8: x = 169917
#Iteration 9: x = 153589