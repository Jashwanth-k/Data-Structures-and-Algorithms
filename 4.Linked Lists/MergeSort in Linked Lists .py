class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

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

def merge(head1,head2):
#this function same as merging function which merges two sorted LL
    fh = ft = None
    if head1.data < head2.data:
        fh = ft = head1
        head1 = head1.next
    else:
        #head2.data <= head1.data
        fh = ft = head2
        head2 = head2.next

    while head1 != None and head2 != None:
        if head1.data < head2.data:
            ft.next = head1
            ft = ft.next
            head1 = head1.next
        else:
            #head2.data <= head1.data
            ft.next = head2
            ft = ft.next
            head2 = head2.next

    if head1 is not None:
        ft.next = head1
    else:
        #head2 is not None
        ft.next = head2

    return fh

def MergeSort_LL(head):
#base case if head.next is None returns head i.e last element of LL
#if head == None is special case for input given as null
    if head == None or head.next == None:
        return head

#finds mid value
    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    mid = slow

#splits the LL into two parts using mid
    head2 = mid.next
    mid.next = None
    head1 = head

    head1 = MergeSort_LL(head1)
    head2 = MergeSort_LL(head2)

    fh = merge(head1,head2)

    return fh

head = MergeSort_LL(head)
printLL(head)