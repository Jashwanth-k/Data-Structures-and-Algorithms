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

def reverse_LL(head):
    if head is None or head.next is None:
        return head,head
#smallhead,smalltail returns head and tail of LL
    smallhead,smalltail = reverse_LL(head.next)
    smalltail.next = head
    head.next = None
    return smallhead,head
#We should return smallhead and head in line nbr 41. Because here head is smallhead and
# Tail is head which we will add ourself last of the LL

head,tail = reverse_LL(head)
printLL(head)