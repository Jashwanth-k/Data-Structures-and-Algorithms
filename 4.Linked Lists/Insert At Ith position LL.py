class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def length(head,c):
    if head == None:
        return c
    return length(head.next,c+1)

def insert_At_Ith(head,i,data):
    if i < 0 or i > length(head,0):
        return head

    count = 0
    prev = None
    curr = head
    while count < i:
        prev = curr
        curr = curr.next
        count+=1

    newNode = Node(data)
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
    newNode.next = curr

    return head

def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head = head.next
    print('None')
    return

def takeInput():

    newList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in newList:
        if currData == -1:
            break
        newNode = Node(currData)

        if head == None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = tail.next

    return head

head = takeInput()
printLL(head)
head = insert_At_Ith(head,1,6)
printLL(head)
head = insert_At_Ith(head,0,9)
printLL(head)
head = insert_At_Ith(head,7,10)
printLL(head)