def equilibrium(a):
    total_sum = i = leftsum =0
    while i < len(a):    #this while loop count the total sum of array
        total_sum+= a[i]
        i+=1

    index = 0            # index of the array
    while index < len(a):   #this while loop runs the index from 0 to n
        rightsum = total_sum - leftsum - a[index]
        # now rightsum will be the total sum - leftsum - the index element
        if leftsum == rightsum:
            return index
        leftsum+= a[index]
        #leftsum will be added with the current index element
        index+=1

    return -1

a = [1,3,4,2,2,5,4,1]
print(equilibrium(a))