import time
def bubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):   # i is already present so len(a)-i. and [-1] to avoid error list index out of range
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

def createlist(n):
    a = []
    for i in range(n,0,-1):
        a.append(i)
    return a
n = int(input('enter :'))
a = createlist(n)
start = time.time()
bubbleSort(a)
end = time.time()
print(end-start)