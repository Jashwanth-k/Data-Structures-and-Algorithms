import queue

s = [1,2,3]

s.append(4)
s.append(5)

print(s.pop())
print(s.pop())
print()

q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)

while q.empty() is False:
    print(q.get())
print()

q = queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
q.put(5)

print(q.qsize())

while q.empty() is False:
    print(q.get())