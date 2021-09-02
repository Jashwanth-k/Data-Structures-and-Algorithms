#T.C O[n]
#in this algo duplicates in list must be absent
def pair_sum(a,N):
    c = 0
    for i in range(len(a)):
        total_sum = N - a[i]
# total_sum is given (sum N) - a[i] and if any element present in list equals to
# total_sum c+=1, ex: 7-2 = 5.present at index 1 then count++
        if total_sum in a:
            c+=1
            print(a[i],total_sum)

    return c//2

a = [2,5,4,1,6]
N = 7
print(pair_sum(a,N))