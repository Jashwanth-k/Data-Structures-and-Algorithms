class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLL(head):
    curr = head
    while curr is not None:
        print(str(curr.data)+'->',end='')
        curr = curr.next
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

    return head

def find_Node(head,x,i):
    if head is None:
        return -1

    if x == head.data:
        return i

    return find_Node(head.next,x,i+1)


t = int(input('enter the test cases:'))
for i in range(t):
    head = takeInput()
    x = int(input('enter the element to search:'))
    print(find_Node(head,x,0))
