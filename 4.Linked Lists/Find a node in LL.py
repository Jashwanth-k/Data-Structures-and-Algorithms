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

    newList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in newList:
        if currData == -1:
            break
        newNode = Node(currData)

        if head == None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = tail.next

    return head

head = takeInput()
printLL(head)

def search_LL(head,i):
    count = 0
    while head is not None:
        if i == head.data:
            return count
        else:
            count+=1
            head = head.next
    return -1

print(search_LL(head,6))
print(search_LL(head,3))
print(search_LL(head,9))
print(search_LL(head,100))