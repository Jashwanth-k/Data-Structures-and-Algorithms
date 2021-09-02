class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    c = 0
    while head != None:
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

def reverse_LL(head):
    prev = None
# take a pointer which is NONE
    while head is not None:
# store the value of the head in TEMP
        temp = head
# move the head : head.next
        head = head.next
# temp.next is the prev node of the linked list
        temp.next = prev
# move the prev position to the temp position
        prev = temp
# when the head becomes NONE the prev will be returned
    return prev

t = int(input('enter no.of test cases:'))
for i in range(t):
    head = takeInput()
    head = reverse_LL(head)
    printLL(head)