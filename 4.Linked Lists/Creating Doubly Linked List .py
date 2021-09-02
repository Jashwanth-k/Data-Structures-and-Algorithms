class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def printLL(head):
    while head is not None:
        print(str(head.data)+'->'+'<-',end='')
        head = head.next
    print('None')
    return

def printLL_reverse(head):
    curr = tail
    while curr is not None:
        print(str(curr.data)+'-><-',end='')
        curr = curr.prev
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
# the newNode reference of previous will be perv one
            tail.next = newNode
            newNode.prev = tail
            tail = tail.next

    return head,tail

head,tail = takeInput()
printLL(head)
print(tail.prev.data)
print(head.next.data)

printLL_reverse(head)