class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def length(head):
    c = 1
    if head is None:
        return 0
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

def delete_Iterative(head,tail,i):
    if i < 0 or i >= length(head):
        return head,tail

    count = 0
    prev = None
    curr = head
    next = head.next
    while count < i:
        count += 1
        prev = curr
        curr = curr.next
        next = next.next

#this case is for deletion of last Node and updating tail
    if curr is tail:
        prev.next = next
        next.prev = prev
        tail = prev

    if prev is not None:
        prev.next = next
        next.prev = prev

    else:
# the below case is for deletion of first Node and updating head
        tail.next = next
        next.prev = tail
        head = next

    return head,tail

head,tail = delete_Iterative(head,tail,5)
head,tail = delete_Iterative(head,tail,4)
head,tail = delete_Iterative(head,tail,0)
printLL(head)

#tip give input [1 2 3 4 5 6 -1] in order to match with above input cases
printLL_reverse(tail)