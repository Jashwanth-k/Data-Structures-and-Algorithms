class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def length(head):
    c = 0
    while head is not None:
        c+=1
        head = head.next
    return c

def printLL(head):
    while head is not None:
        print(str(head.data) + '-><-', end='')
        head = head.next
    print('None')
    return

def print_reverse_LL(tail):
    while tail is not None:
        print(str(tail.data)+'-><-',end='')
        tail = tail.prev
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
            newNode.prev = tail
            tail = tail.next

    return head,tail

head,tail = takeInput()
printLL(head)

def delete_Iterative(head,tail,i):
#this is same as in singly LL but considering prev
    if i < 0 or i >= length(head):
        return head,head

    count = 0
    prev = None
    curr = head
    next = head.next
    while count < i:
        count += 1
        prev = curr
        curr = curr.next
        next = next.next

#for all cases except deletion of first and last Node's
    if prev != None and next != None:
        prev.next = next
        next.prev = prev
#for deletion of last Node in LL
    elif next == None and prev != None:
        prev.next = next
        tail = prev
#for deletion of first Node in LL
    elif prev == None and next != None:
        head = next
        next.prev = prev
    else:
#special case for input [1]
        return prev,next

    return head,tail

head,tail = delete_Iterative(head,tail,5)
printLL(head)
head,tail = delete_Iterative(head,tail,1)
printLL(head)
head,tail = delete_Iterative(head,tail,0)
printLL(head)
#tip give input [1 2 3 4 5 6 -1]
#and input [1,2]

print_reverse_LL(tail)