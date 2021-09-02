class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def length(head):
    c = 1
    curr = head.next
    while curr is not head:
        c+=1
        curr = curr.next
    return c

def printLL(head):
    while head is not None:
        print(str(head.data)+'-><-',end='')
        head = head.next
    print('None')
    return

def printLL_reverse(head):
    curr = tail
    while curr is not None:
        print(str(curr.data)+'-><-',end='')
        curr = curr.prev
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

        tail.next = head
        head.prev = tail

    return head,tail

head,tail = takeInput()

def insert_Iterative(head,tail,i,data):
    if i < 0 or i > length(head):
        return head,tail

    count = 0
    prev = None
    curr = head
    while count < i:
        count += 1
        prev = curr
        curr = curr.next
    newNode = Node(data)

#insertion at first place of LL
    if prev is None:
        head = newNode
        tail.next = newNode
        newNode.next = curr
        curr.prev = newNode
        newNode.prev = tail
#insertion at last of LL
    elif prev is tail:
        prev.next = newNode
        newNode.next = curr
        newNode.prev = prev
        curr.prev = newNode
        tail = newNode
#remaining all cases
    else:
        prev.next = newNode
        newNode.next = curr
        curr.prev = newNode
        newNode.prev = prev

    return head,tail

head,tail = insert_Iterative(head,tail,2,10)
head,tail = insert_Iterative(head,tail,0,100)
head,tail = insert_Iterative(head,tail,6,200)

printLL(head)
printLL_reverse(tail)