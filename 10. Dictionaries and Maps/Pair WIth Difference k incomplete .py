
def pairWithDiffer_K(l,k):

    d = {}
    count = 0
    for i in l:
        d[i] = d.get(i,0) + 1

    count = 0
    for i in l:
        if (i+k) in d and (i-k) in d:
            if d[i+k] != 0 and d[i-k] != 0:
                if d[i+k] == 1 and d[i-k] == 1:
                    length = d[i-k]
                else:
                    length = d[i+k] + d[i-k]

                for j in range(length):
                    count += 1
                d[i + k] = 0
                d[i - k] = 0

        if (i+k) in d and d[i] != 0 and d[i+k] != 0:
            if d[i] == 1 and d[i+k] == 1:
                length = d[i]
            else:
                length = d[i] + d[i+k]

            for j in range(length):
                count += 1
            d[i+k] = 0

        if (i-k) in d and d[i] != 0 and d[i-k] != 0:
            if d[i] == 1 and d[i-k] == 1:
                length = d[i]
            else:
                length = d[i] + d[i-k]

            for j in range(length):
                count += 1
            d[i-k] = 0

    return count

l = [int(ele) for ele in input().split()]
k = int(input('enter k value:'))
print(pairWithDiffer_K(l,k))
