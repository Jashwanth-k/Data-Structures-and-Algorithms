class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    c = 0
    while head is not None:
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

head = takeInput()
printLL(head)

def bubble_sort(head):
#Bubble sort by swapping Nodes

    for i in range(length(head)-1,0,-1):
        prev = None
        curr = head
        next = head.next
        for j in range(i):
            if curr.data > curr.next.data:
#if first element is None
                if prev is None:
                    curr.next = next.next
                    next.next = curr
                    head = next

                    prev = next
                    curr = curr
                    next = curr.next

#for all cases
                else:
                    prev.next = next
                    curr.next = next.next
                    next.next = curr

                    prev = prev.next
                    curr = curr
                    next = curr.next

#if they already in proper order
            else:
                prev = curr
                curr = curr.next
                next = next.next


    return head

head = bubble_sort(head)
printLL(head)