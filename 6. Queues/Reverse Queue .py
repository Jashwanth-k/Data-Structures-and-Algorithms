import queue

q1 = queue.Queue()
q2 = queue.Queue()

q1.put(1)
q1.put(2)
q1.put(3)
q1.put(4)

#here count should maintian and stop the recursion until count becomes '1' or '0'

def reverse_Queue(q1,q2,count):
    if count <= 1:
        return

    count -= 1
    firstElement = q1.get()
    while q1.qsize() != 0:
        q2.put(q1.get())

    while q2.qsize() != 0:
        q1.put(q2.get())

    reverse_Queue(q1,q2,count)
    q1.put(firstElement)


reverse_Queue(q1,q2,q1.qsize())

while q1.empty() is False:
    print(q1.get(),end=' ')