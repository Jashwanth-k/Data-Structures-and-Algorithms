
def subsets_array(arr,si=0):  #si is index of array

    if si >= len(arr):
        output = [[]]
        return output

    smalloutput = subsets_array(arr,si+1)
    output = smalloutput[:]

    for i in smalloutput:
        output.append([arr[si]]+i)    #combining lists

    return output

n = int(input())
arr = [int(ele) for ele in input().split()]
output = subsets_array(arr)
print(output)

for i in output:
    for j in i:
        print(j,end=' ')
    print()

