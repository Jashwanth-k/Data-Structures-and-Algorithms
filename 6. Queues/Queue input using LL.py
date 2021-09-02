from QueueUsingLL import *

q = Queue()

q.enqueue(1)
q.enqueue(5)
q.enqueue(3)
q.enqueue(4)

while q.isEmpty() is False:
    print(q.front())
    q.dequeue()

print(q.front())