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

    return head,tail

head,tail = takeInput()

def reverse(head):
#reverse function retuns head,tail after reversed
    if head is None or head.next is None:
        return head,head

    smallhead,smalltail = reverse(head.next)
    smalltail.next = head
    head.next = None

    return smallhead,head

def kReverse(head,tail,k):
    if k == 1 or tail.next == None:
        h2 = t2 = tail.next
        tail.next = None
        head,tail = reverse(head)
        return head,tail

    head,tail = kReverse(head,tail.next,k-1)

    return head,tail

k = int(input('enter k value :'))

h1 = t1 = head
h1,t1 = kReverse(h1,t1,k)

printLL(h1)
printLL(t1)