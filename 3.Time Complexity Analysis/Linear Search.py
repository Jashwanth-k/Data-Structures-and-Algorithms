def linear(a,x):
    for i in range(len(a)):
        if a[i] == x:
            return 'Index at:',i
    return False
a = [34,5,8,46,2]
x = 8
print(linear(a,x))