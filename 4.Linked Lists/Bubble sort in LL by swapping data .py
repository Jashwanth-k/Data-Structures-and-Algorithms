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

def bubble_sort(head):
#bubble sort algorihthm is same as in case of sorting in array or list but
#in case of Linked List swapping of data is done instead of pointers

    for i in range(length(head)):
        curr = head
        next = head.next
        for j in range(length(head)-i-1):
            if curr.data > next.data:
                curr.data,next.data = next.data,curr.data

            curr = curr.next
            next = next.next

    return head

head = bubble_sort(head)
printLL(head)