class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def length(head):
    c = 1
    curr = head.next
    while curr is not head:
        c+=1
        curr = curr.next
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

def delete_recursive(head,prev,i):
    if i < 0 or i >= length(head):
        return head

    elif head is None:
        return head

    elif i == 0:
        if prev is not None:
            return head.next
        else:
            tail.next = head.next
            return head.next

    smallhead = delete_recursive(head.next,head,i-1)
    head.next = smallhead
    return head

#tip give input [1 2 3 4 5 6 -1]
head = delete_recursive(head,None,0)
head = delete_recursive(head,None,4)

printLL(head)