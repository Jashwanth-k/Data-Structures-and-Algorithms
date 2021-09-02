class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def length_LL(head):
    c = 1
    tail = head.next
    while tail is not head:
        c+=1
        tail = tail.next
    return c

def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head = head.next
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
        tail.next = head

    return head,tail

head,tail = takeInput()

def insert_Iterative(head,i,data,tail):
#insertion is same as in singly LL but we need to handle two cases
#i.e for insertion at first place
    if i < 0 or i > length_LL(head):
        return head,tail

    count = 0
    prev = None
    curr = head
    while count < i:
        count+=1
        prev = curr
        curr = curr.next
    newNode = Node(data)

#below case is for insertion at first place of LL
    if prev is None:
        tail.next = newNode
        newNode.next = head
        head = newNode

#this is for all cases
    else:
        prev.next = newNode
        newNode.next = curr

    return head,tail

head,tail = insert_Iterative(head,0,11,tail)
head,tail = insert_Iterative(head,1,10,tail)
head,tail = insert_Iterative(head,6,20,tail)

#tip give input [1 2 3 4 -1]
printLL(head)