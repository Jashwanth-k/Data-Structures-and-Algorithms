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

head1 = takeInput()
head2 = takeInput()
printLL(head1)
printLL(head2)
# Merge two sorted Linked Lists
#fh = first head and ft = first tail
def merge(head1,head2):
    fh = ft = None
    if head1.data < head2.data:
        fh = ft = head1
        head1 = head1.next
    else:
        #head2.data < head1.data
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

head3 = merge(head1,head2)
printLL(head3)