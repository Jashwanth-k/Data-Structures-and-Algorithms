class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def printLL(head):
    while head is not None:
        print(str(head.data)+'->'+'<-',end='')
        head = head.next
    print('None')
    return

def printLL_reverse(tail):
    curr = tail
    while tail is not None:
        print(str(tail.data)+'-><-',end='')
        tail = tail.prev
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

    return head,tail

head,tail = takeInput()

def insert_recursive(head,tail,i,data):
#the algo is same as insertion in singly LL but we need to mind about prev
    if i < 0:
        return head,tail

    elif i == 0:
#the below step for all cases
        if head is not None:
            newNode = Node(data)
            newNode.next = head
            head.prev = newNode
            return newNode,tail
#for insertion at last place i.e at length of LL
        else:
            newNode = Node(data)
            newNode.next = head
            return newNode,newNode

    elif head == None:
        return head,head

    smallhead,smalltail = insert_recursive(head.next,tail,i-1,data)
    head.next = smallhead
#the below case is for if index given > length of LL
    if smallhead is None:
        return head,head
    smallhead.prev = head

    return head,smalltail

head,tail = insert_recursive(head,tail,30,20)
printLL(head)
head,tail = insert_recursive(head,tail,0,100)
printLL(head)
head,tail = insert_recursive(head,tail,2,500)
printLL(head)
head,tail = insert_recursive(head,tail,5,200)
printLL(head)

#to match with above input cases give input [1 2 3 -1]
printLL_reverse(tail)