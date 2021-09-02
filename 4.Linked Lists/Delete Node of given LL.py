class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def length(head,c):
    if head == None:
        return c
    return length(head.next,c+1)

def Delete_Node(head,i):
    if i < 0 or i >= length(head,0):
        return head

    count = 0
    prev = None
    curr = head
    next = curr.next
    while count < i:
        prev = curr
        curr = curr.next
        next = next.next
        count+=1
    if prev is not None:
        prev.next = next
    else:
        head = next
    del curr

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
head = Delete_Node(head,2)
printLL(head)
head = Delete_Node(head,2)
printLL(head)
head = Delete_Node(head,0)
printLL(head)