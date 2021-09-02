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

def insert_recursive(head,prev,i,data):
#this algo is same as singly LL but tail.next will be head hence it is curcular
    if i < 0:
        return head

    elif head is None:
        return head

    elif i == 0:
#special case if we want insert at head of LL
        if prev is None:
            newNode = Node(data)
            tail.next = newNode
            newNode.next = head
            return newNode
        else:
            newNode = Node(data)
            newNode.next = head
            return newNode

    smallhead = insert_recursive(head.next,head,i-1,data)
    head.next = smallhead
    return head

head = insert_recursive(head,None,0,10.0)
head = insert_recursive(head,None,2,20)
head = insert_recursive(head,None,6,30.0)
head = insert_recursive(head,None,7,50.0)

#tip give input [1 2 3 4 -1]
printLL(head)