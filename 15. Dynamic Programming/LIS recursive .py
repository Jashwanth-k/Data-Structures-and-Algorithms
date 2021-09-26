
def lis(li,i,n):

    if i >= n:
        return 0,0

    including_max = 1
    for j in range(i+1,n):
        if li[j] > li[i]:
            furthur_including_max = lis(li,j,n)[0]    #to find elements greater then i
            including_max = max(including_max,1 + furthur_including_max)    # 1 is added to furthur including max bcz we are including first element

    excluding_max = lis(li,i+1,n)[1]
    overallMax = max(including_max,excluding_max)
    return including_max,overallMax


li = [int(ele) for ele in input().split()]
n = len(li)
ans = lis(li,0,n)[1]    #output is in the form of tuple
print(ans)
