s = [60, 70, 80, 100, 90, 75, 80, 120]

def Stockspan(s):
#move from last to first
#check last element with all the elements present in list

    for i in range(len(s)-1,-1,-1):
        count = 1
        for j in range(i-1,-1,-1):
            if s[i] > s[j]:
                count += 1
            else:
                break

        s[i] = count

Stockspan(s)
print(s)