class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def length(head):
    c = 1
    curr = head.next
    while curr is not head:
        c+=1
        curr = curr.next
    return c

def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head = head.next
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
        tail.next = head

    return head,tail

head,tail = takeInput()

def delete_Iterative(head,i):
    if i < 0 or i >= length(head):
        return head

    count = 0
    prev = None
    curr = head
    next = head.next
    while count < i:
        count += 1
        prev = curr
        curr = curr.next
        next = next.next

    if prev is not None:
        prev.next = next
    else:
        head = next
        tail.next = head

    return head

head = delete_Iterative(head,0)
head = delete_Iterative(head,2)
head = delete_Iterative(head,3)

#tip give input [1 2 3 4 5 6 -1]
printLL(head)