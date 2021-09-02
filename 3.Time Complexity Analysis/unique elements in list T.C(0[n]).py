#1. XOR of a number with itself is 0.
#2. XOR of a number with 0 is number itself.
def unique_element(a):
    i = xor = 0
    while i < len(a):
        xor = xor^a[i] #xor can be used with ^ symbol
        i+=1
    print(xor)

a = [6,1,6,3,4,3,1]
unique_element(a)