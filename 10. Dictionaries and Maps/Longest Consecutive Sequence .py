
def longest_sequence(l):

    d = {}
    for i in l:
        d[i] = True

    maxlength = 0
    start = 0
    for curr in d:
        length = 0
        i = curr
        d[curr] = False #if we check the elements change it's value to False

        while (i+1) in d and d[i+1] != False: #for finding elements > curr
            length += 1
            d[i + 1] = False
            i = i + 1

        while (curr-1) in d and d[curr-1] != False: #for finding elements < curr
            length += 1
            d[curr - 1] = False
            curr = curr - 1

        if length > maxlength:
            maxlength = length
            start = curr

    print(start,maxlength + start)

l = [int(ele) for ele in input().split()]
longest_sequence(l)
