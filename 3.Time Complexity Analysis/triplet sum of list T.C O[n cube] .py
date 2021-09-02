#T.C is O[n**2]
def triplet_sum(a,n):
    c = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            for k in range(j+1,len(a)):
                if a[i] + a[j] + a[k] == n:
                    c+=1
#here i is a element from list and it runs j from i+1 to n then k runs from
#j+1 to n if sum of a[i],a[j],a[k] == n count is incremented

    return c
a = [1,2,3,4,5,6,7]
n = 12
print(triplet_sum(a,n))