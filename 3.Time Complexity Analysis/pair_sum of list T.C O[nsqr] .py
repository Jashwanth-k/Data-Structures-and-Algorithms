#T.C is O[nsqr] since i is added with i elements i.e n*n is n**2
#we should find the sum of 2 elements in list is == 7
def pair_sum(a,N):
    count = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if i != j:
                if a[i] + a[j] == N:
                    count+=1
#if pair sum equals count is ++
    return count

a = [1,3,6,2,5,4,3,2,4]
N = 7
print(pair_sum(a,N))