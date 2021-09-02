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

def delete_Nnodes(head,m,n):
    t1 = head
    t2 = head
#special cases
    if n == 0:
        return head
    if m == 0:
        return

    while head is not None:
        c1 = 1
        while c1 < m and t1 != None:
            c1 += 1
            t1 = t1.next

#if t1 become None returns head
        if t1 is None:
            return head

        c2 = 1
        t2 = t1.next
        while c2 < n and t2 != None:
            c2 += 1
            t2 = t2.next

#if t2 becomes None t1.next is None and returns head
        if t2 is None:
            t1.next = t2
            return head

        t2 = t2.next
        t1.next =t2
        t1 = t2

m = int(input('enter m:'))
n = int(input('enter n:'))

head = delete_Nnodes(head,m,n)
printLL(head)