class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_Ith(head,c,i):
    while head != None and c <= i:
        if c == i:
            print(head.data)
        c+=1
        head = head.next
    return

def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)

        if head == None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode

    return head

head = takeInput()
i = int(input('enter i:'))
print_Ith(head,0,i)