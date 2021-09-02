class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def printLL(head):
    while head is not None:
        print(str(head.data)+'-><-',end='')
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
            tail.next = newNode
            newNode.prev = tail
            tail = tail.next

        tail.next = head
        head.prev = tail

    return head,tail

head,tail = takeInput()

def delete_recursive(head,tail,i,prev):
    if i < 0:
        return head,tail

    if i == 0:
#this case is for deletion of first Node
        if prev is None:
            tail.next = head.next
            head.next.prev = tail
            return head.next,tail

#the below case is for deletion of last Node and update tail
        elif prev.next is tail:
            return head.next,head.prev

        else:
            return head.next,tail

    smallhead,smalltail = delete_recursive(head.next,tail,i-1,head)
    head.next = smallhead
    smallhead.prev = head

    return head,smalltail

head,tail = delete_recursive(head,tail,5,None)
head,tail = delete_recursive(head,tail,0,None)
head,tail = delete_recursive(head,tail,2,None)

print(head.data)
print(tail.data)

printLL(head)
printLL_reverse(head)