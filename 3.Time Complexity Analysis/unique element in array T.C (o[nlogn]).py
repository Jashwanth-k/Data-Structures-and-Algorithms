import time
def unique_element(a):
    a = sorted(a)  #we should use mergesort of quick instead of this line
    a1 = list(a)
    for i in range(len(a)-1):  #this loop runs from 0 to n-1
        if a[i] == a[i+1]:
            a1.remove(a[i])    #if equals removes a[i] and a[i+1] from list a2
            a1.remove(a[i+1])
#in this we didn't removed a[i] because it gives error since len(a) decreases with removal
    
    print(a1)

n = int(input('enter n :'))
def createArraya1(n):
    a = []
    for i in range(n,0,-1):
        a.append(i)
    return a
a = createArraya1(n)
s = time.time()
unique_element(a)
e = time.time()
print(e-s)