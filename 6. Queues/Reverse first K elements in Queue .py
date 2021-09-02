import queue

q1 = queue.Queue()
q2 = queue.Queue()

k = int(input('enter k value:'))
input = [ele for ele in input().split()]
for i in input:
    q1.put(i)

#we should reverse the elements for 'k' times
def reverseK_elements(q1,q2,k):
    if k <= 0:
        return

    k -= 1
    firstElement = q1.get()
    while q1.qsize() != 0:
        q2.put(q1.get())

    while q2.qsize() != 0:
        q1.put(q2.get())

    reverseK_elements(q1,q2,k)
    q1.put(firstElement)

reverseK_elements(q1,q2,k)

#after reversing the 'k' elements we should call get() and put() functions
#for [n-k] times n = len(q1)
for i in range(q1.qsize()-k):
    data = q1.get()
    q1.put(data)

while q1.empty() is False:
    print(q1.get(),end=' ')