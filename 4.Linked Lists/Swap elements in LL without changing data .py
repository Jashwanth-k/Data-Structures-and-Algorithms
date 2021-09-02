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

def swap_Nodes(head,i,j):
#take four variables prev,prev2,curr1,curr2 and assign prev1,prev2 = None
#which are will prev of curr elements
#assign curr1,curr2 = head

    p1 = p2 = None
    c1 = c2 = head
    count1 = count2 = 0
    if i -j == 0:
        return head

    while count1 < i and c1 != None:
        count1 += 1
        p1 = c1
        c1 = c1.next

    while count2 < j and c2 != None:
        count2 += 1
        p2 = c2
        c2 = c2.next

#if 'i' is 0 and 'j-i' is 1 this represents we need to swap first two elements of LL
    if i == 0 or j == 0:
        if j-1 == 0 or i-j == 0:
            c1.next = c2.next
            c2.next = c1
            return c2
#in this case we need to swap first element and last element of LL. since i = 0 and c2.next is None
        if c2.next is None:
            c2.next = c1.next
            p2.next = c1
            c1.next = None
            return c2

#in this case the elements in LL are adjacent
    elif j-i == 1 or i-j == 1:
        p1.next = c2
        c1.next = c2.next
        c2.next = c1

#the below case is to swap first element and remaining any random element in LL
    elif i == 0 or j == 0:
        p2.next = c1.next
        c1.next = c2.next
        c2.next = p2
        p2.next.next = c1
        return c2

#this is for if we need to swap last element with any other random element. Excluding head
    elif c2.next is None:
        c2.next = c1.next
        p2.next = c1
        c1.next = None
        return c2

    else:
        p1.next = c2
        p2.next = c1
        c1.next = c2.next
        c2.next = p2


    return head

i = int(input('enter i :'))
j = int(input('enter j :'))
head = swap_Nodes(head,i,j)
printLL(head)