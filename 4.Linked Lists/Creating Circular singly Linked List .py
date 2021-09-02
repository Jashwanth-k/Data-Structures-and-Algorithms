class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head = head.next
    print('None')
    return

def length_LL(head):
    if head == None:
        return 0
    curr = head.next
    c = 1
    while curr is not head:
        curr = curr.next
        c+=1
    return c

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
#circular singly LL is same as single LL but whose tail.next will be head
    return head,tail

head,tail = takeInput()
print(length_LL(head))
print(length_LL(tail))

