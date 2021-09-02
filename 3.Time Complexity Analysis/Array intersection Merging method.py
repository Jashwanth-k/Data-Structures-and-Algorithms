def intersection(a1,a2):
    a1 = sorted(a1)
    a2 = sorted(a2)
    i = j = 0
    while i < len(a2) and j < len(a2):
        if a1[i] < a2[j]:
            i+=1
        elif a2[j] < a1[i]:
            j+=1
        else:
            print(a1[i])
            i+=1
            j+=1


a1  = [4, 9, 1, 17, 11, 26, 28, 54, 69]
a2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
intersection(a1,a2)