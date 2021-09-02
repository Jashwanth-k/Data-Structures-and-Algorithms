
def PairSumto0(list):

#here D is the Dictionary
    d = {}
    for i in list:        #traverse through the list
        if (-i) in d:
            for j in range(d[-i]):  #if present in Dict print frequency times of d[-i]
                print(i,-i)

        d[i] = d.get(i,0) + 1

    print(d)

inputlist = [int(ele) for ele in input().split()]
PairSumto0(inputlist)
