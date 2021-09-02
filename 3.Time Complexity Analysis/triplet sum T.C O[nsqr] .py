#T.C is O[n*2]
def triplet_sum(a,N):
# list must be sorted for this algo and should use mergesort or q.s
    a.sort()
    c = 0
    for i in range(len(a)-2):
# i runs from 0 to n-2 since si and ei are present. They occupy the last 2 elements
#place in worst case
        si = i+1
        ei = len(a)-1
        while si < ei:
            if a[i] + a[si] + a[ei] == N:
                c+=1
                print(a[i],a[si],a[ei])
                si+=1
                ei-=1
            elif a[i] + a[si] + a[ei] < N:
                si+=1
            else: #a[i] + a[si] + a[ei] > N
                ei-=1
    return c

a = [-6,-5,-3,0,2,5,8,10,11]
N = 10
print(triplet_sum(a,N))