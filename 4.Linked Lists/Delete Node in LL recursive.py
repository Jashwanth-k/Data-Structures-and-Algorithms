class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def delete_recursive(head,i):
    if i < 0:
        return head
    elif head == None:
#if Head is None given as base case rather than i == 0 because it gives error if we try to Delete at length of LL
        return
    elif i == 0:
        return head.next

    smallHead = delete_recursive(head.next,i-1)
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
head = delete_recursive(head,2)
printLL(head)
head = delete_recursive(head,0)
printLL(head)
head = delete_recursive(head,3)
printLL(head)
head = delete_recursive(head,30)
printLL(head)
head = delete_recursive(head,2)
printLL(head)