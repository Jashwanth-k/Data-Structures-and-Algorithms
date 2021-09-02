def ascending(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] < a[j]:
                a[i],a[j] = a[j],a[i]

a = [34,23,7,5,54,3]
ascending(a)
print(a)