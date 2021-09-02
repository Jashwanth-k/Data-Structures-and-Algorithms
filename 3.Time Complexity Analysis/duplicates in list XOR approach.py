#T.C 0[n]
#If we XOR a number by itself, even number of times then it will give you 0.
# If we XOR a number with itself, odd number of times, then it will give you the number
#itself.
def duplicates_list(a):
    ans = 0
    for i in range(len(a)):
        ans = ans^a[i]
    i = 0
    while i <= len(a)-2:
        ans = ans^i
        i+=1
    return ans
#Also XOR of a number with 0 gives you that number again.

a = [0,1,3,2,2]
b = duplicates_list(a)
print(b)