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

def tail_smallhead(smallhead):
    while smallhead.next is not None:
        smallhead = smallhead.next
    return smallhead

def reverse_LL(head):
#if you are given a LL if input NUll this will return None
#If we are given a LL of LENGTH [1] this returns head which the only NODE in LL
    if head == None or head.next == None:
        return head

    smallhead = reverse_LL(head.next)
#TAIL calls the function executes and returns tail for each smallhead
    tail = tail_smallhead(smallhead)
    tail.next = head
    head.next = None
    return smallhead

head = reverse_LL(head)
printLL(head)