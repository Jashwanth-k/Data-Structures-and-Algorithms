class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLL(head):
    curr = head
    while curr is not None:
        print(str(curr.data)+'->',end='')
        curr = curr.next
    print('None')
    return

def takeInput():

    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currdata in inputList:
        if currdata == -1:
            break
        newNode = Node(currdata)

        if head == None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = tail.next

    return head

head = takeInput()

def reverse(head):
#reverse function retuns head,tail after reversed
    if head is None or head.next is None:
        return head,head

    smallhead,smalltail = reverse(head.next)
    smalltail.next = head
    head.next = None

    return smallhead,head

def move_pointers(head,k):
#this funtion moves head and tail w.r.t value of k
    curr = head
    count = 1
    while count < k and curr != None:
        count += 1
        curr = curr.next
    return head,curr

def kReverse(head,k):

    h1 = t1 = head
    h1,t1 = move_pointers(h1,k)
    if t1 is None:
        h1,t1 = reverse(h1)
        return h1

    h2 = t2 = t1.next
    t1.next = None
    h1,t1 = reverse(head)

    h2,t2 = move_pointers(h2,k)
    if t2 is None:
        h2,t2 = reverse(h2)
        t1.next = h2
        return h1

    h3 = t3 = t2.next
    t2.next = None
    h2,t2 = reverse(h2)

    h3,t3 = move_pointers(h3,k)
    if t3 is None:
        h3,t3 = reverse(h3)
        t1.next = h2
        t2.next = h3
        return h1

    h4 = t4 = t3.next
    t3.next = None
    h3,t3 = reverse(h3)

    h4,t4 = move_pointers(h4,k)
    if t4 is None:
        h4,t4 = reverse(h4)
        t1.next = h2
        t2.next = h3
        t3.next = h4
        return h1

    h5 = t5 = t4.next
    t4.next = None
    h4,t4 = reverse(h4)

    h5,t5 = move_pointers(h5,k)
    if t5 is None:
        h5,t5 = reverse(h5)
        t1.next = h2
        t2.next = h3
        t3.next = h4
        t4.next = h5
        return h1

    h6 = t6 = t5.next
    t5.next = None
    h5,t5 = reverse(h5)

    t1.next = h2
    t2.next = h3
    t3.next = h4
    t4.next = h5
    t5.next = h6

    return h1

k = int(input('enter k value :'))
h1 = kReverse(head,k)
printLL(h1)