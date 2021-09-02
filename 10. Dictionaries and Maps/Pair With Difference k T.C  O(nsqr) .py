
def pairDiffer_K(l,k):

    count = 0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] + k == l[j] or l[i] - k == l[j]:
                count += 1

    print(count)

l = [int(ele) for ele in input().split()]
k = int(input('enter k value:'))
pairDiffer_K(l,k)

