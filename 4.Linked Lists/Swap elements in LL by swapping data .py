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
    temp1 = temp2 = head
    count1 = count2 = 0

    while count1 < i:
        count1 += 1
        temp1 = temp1.next

    while count2 < j:
        count2 += 1
        temp2 = temp2.next

    if temp1 != None and temp2 != None:
        temp1.data,temp2.data = temp2.data,temp1.data

    return head

i = int(input('enter i :'))
j = int(input('enter j :'))

head = swap_Nodes(head,i,j)
printLL(head)