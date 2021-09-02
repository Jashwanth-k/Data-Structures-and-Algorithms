class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insert_recursive(head,i,data):
    if i < 0:
        return head
    elif i == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode
# Here i == 0 given as base case because we just wanna insert at length of LL i.e last element
    elif head == None:
        return None

    smallHead = insert_recursive(head.next,i-1,data)
    head.next = smallHead
    return head

def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head = head.next
    print('None')
    return

def takeInput():

    newList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in newList:
        if currData == -1:
            break
        newNode = Node(currData)

        if head == None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = tail.next

    return head

head = takeInput()
printLL(head)
head = insert_recursive(head,2,6)
printLL(head)
head = insert_recursive(head,0,9)
printLL(head)
head = insert_recursive(head,7,10)
printLL(head)