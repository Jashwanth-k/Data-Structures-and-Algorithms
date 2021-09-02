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

def printLL_reverse(tail):
    curr = tail
    while tail is not None:
        print(str(tail.data)+'-><-',end='')
        tail = tail.prev
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

    return head,tail

head,tail = takeInput()

def delete_recursive(head,tail,i):
     if i < 0:
         return head,tail
#this case is for if index i > length of LL
     elif head is None:
         return head,head

     elif i == 0:
         if head.next is not None:
             head.next.prev = None
             return head.next,tail
#the below case is for deletion of last Node
         else:
             tail = head
             return head.next,tail

     smallhead,smalltail = delete_recursive(head.next,tail,i-1)
     head.next = smallhead
#here instead of tail - head is given below bcz when head.next is None,tail will be the head
     if smallhead is None:
         return head,head

     smallhead.prev = head
     return head,smalltail

head,tail = delete_recursive(head,tail,3)
printLL(head)
head,tail = delete_recursive(head,tail,2)
printLL(head)
head,tail = delete_recursive(head,tail,0)
printLL(head)

#tip give input [1,2,3,4] to match with above input cases
printLL_reverse(tail)