
#recursive
def reverse_n(nbr,len):

    if nbr < 0:
        return 0

    if nbr < 10:
        return nbr

    res = nbr % 10      #last digit
    ans = 10 ** len     #multiply * length-1
    output = res*ans
    return output + reverse_n(nbr//10,len-1)

n = int(input())
l = len(str(n))-1
print(reverse_n(n,l))

#iterative
n = int(input())
res = 0
while n > 0:
    a = n % 10
    res = res*10 + a
    n = n // 10

print(res)


