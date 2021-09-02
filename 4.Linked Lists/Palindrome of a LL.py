class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    c = 0
    while head != None:
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

def break_LL(head):
#here mid = (len-1)//2 considering even and odd cases
    mid = (length(head)-1)//2
    i = 0
    curr = head
    while i < mid:
        curr = curr.next
        i+=1
    mid = curr

#this breaks LL into two parts using mid
    head2 = mid.next
    mid.next = None
    head1 = head

    return head1,head2

head1,head2 = break_LL(head)

def reverse_LL(head2):
#this reverses the second part of LL i.e head2 and returns it
    prev = None
    curr = head2
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

head2 = reverse_LL(head2)

def compare_LL(head1,head2):
    #printLL(head1)
    #printLL(head2)
# Comparing the each elements of head1 and head2
    while head1 != None and head2 != None:
        if head1.data != head2.data:
            return False
        else:
            head1 = head1.next
            head2 = head2.next
    return True

print(compare_LL(head1,head2))