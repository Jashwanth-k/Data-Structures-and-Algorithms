

def print_subsets(arr,output=[]):

    if len(arr) == 0:
        #print(output)
        for i in output:
            print(i,end=' ')
        print()
        return

    #don't include first element
    print_subsets(arr[1:],output)
    output = output[:]      #output is updated to avoid repetition of elements

    #include first element
    output.append(arr[0])
    print_subsets(arr[1:],output)

arr = [15, 20, 12]
print_subsets(arr)

#using newoutput helper array
def print_subsets(arr,output=[]):

    if len(arr) == 0:
        for i in output:
            print(i,end=' ')
        print()
        return

    print_subsets(arr[1:],output)

    newoutput = output[:]
    newoutput.append(arr[0])
    print_subsets(arr[1:],newoutput)

arr = [15, 20, 12]
print_subsets(arr)