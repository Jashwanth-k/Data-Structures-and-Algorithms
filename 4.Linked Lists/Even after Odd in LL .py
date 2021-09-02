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

head = takeInput()
printLL(head)

def even_odd(head):
    oddhead = oddtail = None
    evenhead = eventail = None
    while head is not None:
        if head.data % 2 != 0:
            if oddhead is None:
                oddhead = oddtail = head
            else:
                oddtail.next = head
                oddtail = oddtail.next
            head = head.next
            oddtail.next = None
#the oddtail.next will be None in order to break the LL

        else:
            if evenhead is None:
                evenhead = eventail = head
            else:
                eventail.next = head
                eventail = eventail.next
            head = head.next
            eventail.next = None
#eventail.next is None to break the LL afer the head

#if the input given only in even numbers the retuen evenhead
    if oddhead is not None:
        oddtail.next = evenhead
        return oddhead

    else:
        return evenhead

head = even_odd(head)
printLL(head)