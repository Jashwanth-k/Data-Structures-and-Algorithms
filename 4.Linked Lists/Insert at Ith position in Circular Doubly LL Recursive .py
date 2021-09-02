class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def printLL(head):
    while head is not None:
        print(str(head.data)+'-><-',end='')
        head = head.next
    print('None')
    return

def printLL_reverse(head):
    curr = tail
    while curr is not None:
        print(str(curr.data)+'-><-',end='')
        curr = curr.prev
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
            newNode.prev = tail
            tail = tail.next

        tail.next = head
        head.prev = tail

    return head,tail

head,tail = takeInput()

def insert_recursive(head,tail,i,data,prev):
    if i < 0:
        return head,tail

    if i == 0:
#this case is insetion at last place i.e tail of LL
        if prev is tail:
            newNode = Node(data)
            newNode.next = head
            head.prev = newNode
            return newNode,newNode

#the below case for insertion at first place i.e at head of LL
        elif prev is None:
            newNode = Node(data)
            tail.next = newNode
            newNode.next = head
            newNode.prev = tail
            head.prev = newNode
            return newNode,tail

        else:
            newNode = Node(data)
            newNode.next = head
            head.prev = newNode
            return newNode,tail

    elif head is None:
        return head,head

    smallhead,smalltail = insert_recursive(head.next,tail,i-1,data,head)
    head.next = smallhead
    smallhead.prev = head

    return head,smalltail

head,tail = insert_recursive(head,tail,0,10,None)
head,tail = insert_recursive(head,tail,5,20,None)
head,tail = insert_recursive(head,tail,3,100,None)

printLL(head)
#tip give input [1 2 3 4 -1]
printLL_reverse(tail)