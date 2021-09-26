

def mincost_path(arr,i=0,j=0):

    m = len(arr)
    n = len(arr[0])

    if i == m-1 and j == n-1:   #special case
        return arr[i][j]

    if i >= m or j >= n:        #base case
        return float('inf')

    ans1 = mincost_path(arr,i+1,j)    #down
    ans2 = mincost_path(arr,i,j+1)    #right
    ans3 = mincost_path(arr,i+1,j+1)  #diagonal wise

    output = arr[i][j] + min(ans1,ans2,ans3)
    return output


str = input().split()
m,n = int(str[0]),int(str[1])

arr = [[int(ele) for ele in input().split()] for i in range(m)]
print(mincost_path(arr))

