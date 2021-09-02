def intersection(a1,a2):
    i = j = 0
    a3 = []
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            if a1[i] not in a3:
                a3.append(a1[i])
            i+=1
        elif a2[j] < a1[i]:
            if a2[j] not in a3:
                a3.append(a2[j])
            j+=1
        else:
            if a2[j] not in a3:
                a3.append(a2[j])
            j+=1
    while j < len(a2):
        if a2[j] not in a3:
            a3.append(a2[j])
        j+=1
        i+=1
    print(a3)

arr1 = [1,2,2,4, 5,5,5,5, 6]
arr2 = [7,8,9,9]
intersection(arr1,arr2)