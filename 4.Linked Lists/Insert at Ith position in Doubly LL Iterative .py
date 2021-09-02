class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def printLL(head):
    while head is not None:
        print(str(head.data)+'->'+'<-',end='')
        head = head.next
    print('None')
    return

def printLL_reverse(tail):
    curr = tail
    while tail is not None:
        print(str(tail.data)+'-><-',end='')
        tail = tail.prev
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
            newNode.prev = tail
            tail = tail.next

    return head,tail

head,tail = takeInput()
printLL(head)

def length(head):
    c = 0
    while head is not None:
        c+=1
        head = head.next
    return c

def insert_iterative(head,tail,i,data):
#insertion same as single LL but we need to consider the prev of newNode
    if i < 0 or i > length(head):
        return head,tail

    count = 0
    prev = None
    curr = head
    while count < i:
        count+=1
        prev = curr
        curr = curr.next
    newNode = Node(data)

#for all casres except for insertion at first and last palce in LL
    if prev != None and curr != None:
        prev.next = newNode
        newNode.next = curr
        curr.prev = newNode
        newNode.prev = prev

#for insertion at first place i.e at head
    elif prev == None and curr != None:
        newNode.next = curr
        newNode.prev = prev
        curr.prev = newNode
        head = newNode

#for insertion at last place i.e at tail
    elif curr == None and prev != None:
        prev.next = newNode
        newNode.next = curr
        newNode.prev = prev
        tail = newNode

    return head,tail

head,tail = insert_iterative(head,tail,1,11)
printLL(head)
head,tail = insert_iterative(head,tail,0,15)
printLL(head)
head,tail = insert_iterative(head,tail,5,20)
printLL(head)
head,tail = insert_iterative(head,tail,3,100)
printLL(head)
#tip give input [1 2 3 -1] to match all the above cases
#input [1,2]
#input [1]

printLL_reverse(tail)