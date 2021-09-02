class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    while head is not None:
        print(str(head.data) + '->', end='')
        head = head.next
    print('None')
    return

def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)

        if head == None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode

    return head

def Eliminate_duplicates(head):
    if head == None or head.next == None:
        return head
#if head is null or head.next is None there is no need to check further becz LL didn't have duplicates
    t1 = head
    t2 = head.next
    while t2 != None:
        if t1.data == t2.data:
            t2 = t2.next
# here is t1 == t2 : t2 is moved till it finds an element which is != t1
        else:
# if t1 != t2 : t1.next is assigned with 't2' then 't1' goes to the position of t2 further loop continues
            t1.next = t2
            t1 = t2

    t1.next = t2
    return head

t = int(input('enter the no.of test cases:'))
for i in range(t):
    head = takeInput()
    head = Eliminate_duplicates(head)
    printLL(head)