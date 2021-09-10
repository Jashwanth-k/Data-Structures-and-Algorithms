

def subsets_sumtoK(arr,k,output=[]):

    if len(arr) == 0:
        if k == 0:
            print(output)
        return

    #exclude first element of array
    subsets_sumtoK(arr[1:],k,output)


    #include first element of array
    #assume first element is present subtract the first element from k
    newoutput = output[:]
    newoutput.append(arr[0])
    subsets_sumtoK(arr[1:],k-arr[0],newoutput)


arr = [int(ele) for ele in input().split()]
k = int(input())
subsets_sumtoK(arr,k)

'''input format
5 12 3 17 1 18 15 3 17
6'''
