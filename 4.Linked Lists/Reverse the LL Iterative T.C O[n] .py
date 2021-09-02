class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    c = 0
    while head is not None:
        c+=1
        head = head.next
    return c

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

head = takeInput()
printLL(head)

def reverse(head):
    curr = head
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

head = reverse(head)
printLL(head)