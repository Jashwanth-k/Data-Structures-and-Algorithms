class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length_recursive(head,c):
    if head == None:
        return c
    return length_recursive(head.next,c+1)

def length_iterative(head,c):
    c = 0
    while head is not None:
        c+=1
        head = head.next
    return c

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
print(length_recursive(head,0))
print(length_iterative(head,0))