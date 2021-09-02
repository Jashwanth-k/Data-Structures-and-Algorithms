def Geometric_sum(k):

    if k == 1:
        return 1+1/2
    smallOutput = Geometric_sum(k-1)
    output = smallOutput + 1/2**k
    return output

k = int(input('enter :'))
print(Geometric_sum(k))