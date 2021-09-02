def equilibrium(a):
    n = len(a)
    for i in range(n):
        leftsum = 0
        rightsum = 0

        for j in range(i): #for left sum of list
            leftsum+=1
        for j in range(i+1,n): #for right sum of list
            rightsum+=1
        if leftsum == rightsum: #if LS == RS prints 'i'
            print(i)

a = [-7, 1, 5,2, -4, 3,0]
(equilibrium(a))