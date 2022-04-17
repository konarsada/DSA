'''

class Queue:
    def __init__(self, n):
        self.q = [None] * n
        self.front = self.rear = 0
        self.n = n
    def enqueue(self, n):
        if(self.rear == self.n):
            print("Overflow")
        else:
            self.q[self.rear] = n
            self.rear += 1
            print(self.q)
    def dequeue(self):
        if(self.front == self.rear):
            print("Underflow")
        else:
            self.q[self.front] = None
            self.front += 1
            print(self.q)

q = Queue(4)
q.enqueue(20)
q.enqueue(25)
q.enqueue(10)
q.dequeue()
q.dequeue()
print(q.rear, q.front)
q.dequeue()

'''

class Queue:
	def __init__(self, c):
		self.queue = []
		self.front = self.rear = 0
		self.capacity = c

	def queueEnqueue(self, data):
		if(self.capacity == self.rear):
			print("Queue is full")
		else:
			self.queue.append(data)
			self.rear += 1

	def queueDequeue(self):
		if(self.front == self.rear):
			print("Queue is empty")
		else:
			x = self.queue.pop(0)
			self.rear -= 1

	# Function to print queue elements
	def queueDisplay(self):
		if(self.front == self.rear):
			print("Queue is Empty")
		for i in self.queue:
			print(i, end = ',')

	# Print front of queue
	def queueFront(self):
		if(self.front == self.rear):
			print("Queue is Empty")

		print("Front Element is:",
			self.queue[self.front])

# Driver code
if __name__=='__main__':

	# Create a new queue of
	# capacity 4
	q = Queue(4)

	# Print queue elements
	q.queueDisplay()

	# Inserting elements in the queue
	q.queueEnqueue(20)
	q.queueEnqueue(30)
	q.queueEnqueue(40)
	q.queueEnqueue(50)

	# Print queue elements
	q.queueDisplay()

	# Insert element in queue
	q.queueEnqueue(60)

	# Print queue elements
	q.queueDisplay()

	q.queueDequeue()
	q.queueDequeue()
	print("\n\nafter two node deletion\n")

	# Print queue elements
	q.queueDisplay()

	# Print front of queue
	q.queueFront()