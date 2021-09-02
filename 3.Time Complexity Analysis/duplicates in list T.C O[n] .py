#time complexity is O[n]
def duplicates_list(a):
    n = len(a)
    total_sum = 0
    for i in range(n):
        total_sum = total_sum + a[i]
#in this method the duplicate value can be found by subtracting the total_sum of
#list with calculated sum for (n-2) elements
    calculated = (n-2)*(n-1)//2
    output = total_sum - calculated
    return output

a = [0,1,3,5,4,3,2]
print(duplicates_list(a))