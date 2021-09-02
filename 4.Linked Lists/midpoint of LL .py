class Node:
    def __init__(self,data):
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
        print(str(head.data)+'->',end='')
        head = head.next
    print('None')
    return

def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = tail = None
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

def mid_point(head):
    mid = (length(head)-1)//2
# mid will be [len-1]//2 bcz considering both even and odd cases for length of LL
    i = 0
    while i < mid:
        head = head.next
        i+=1
    return head.data

def mid_point_LL(head):
#this is the fastest approach
    slow = head
    fast = head
#slow will move 1x speed and fast will move 2x speed
#if fast reaches last or last second position slow will at mid position and returned
    while fast.next != None and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data

print(mid_point(head))
print(mid_point_LL(head))