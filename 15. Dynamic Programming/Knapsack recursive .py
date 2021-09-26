
def knapsack(weight,values,W,i=0):

    if i >= len(values):
        return 0

    if weight[i] <= W:
        #including ith element
        ans1 = values[i] + knapsack(weight,values,W-weight[i],i+1)
        ans2 = knapsack(weight,values,W,i+1)
        ans = max(ans1,ans2)
    else:
        #excluding ith element
        ans = knapsack(weight,values,W,i+1)

    return ans


weight = [int(ele) for ele in input().split()]
values = [int(ele) for ele in input().split()]
W = int(input())
print(knapsack(weight,values,W))

