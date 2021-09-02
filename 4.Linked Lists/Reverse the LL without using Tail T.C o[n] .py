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

head = takeInput()
printLL(head)

def reverse(head):
    if head is None or head.next is None:
        return head
    smallhead = reverse(head.next)
# here the TAIL is head.next itself so tail = head.next
    tail = head.next
    tail.next = head
    head.next = None
    return smallhead

head = reverse(head)
printLL(head)