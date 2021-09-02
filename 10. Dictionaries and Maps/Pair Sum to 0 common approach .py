
def pairSumto0(list):

    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i] + list[j] == 0:
                print(list[i],list[j])

list1 = [int(ele) for ele in input().split()]
(pairSumto0(list1))

def pairSum2(list):

    d = {}
    for i in list:
        d[i] = d.get(i,0) + 1

    for j in list:
        if (-j) in d:
            if d[j] == 1:
                freq = d[-j]
            elif d[-j] == 1:
                freq = d[j]
            else:
                freq = d[j] + d[-j]

            for k in range(freq):
                print(j,-j)
            d[j] = 0
            d[-j] = 0

    print(d)

list2 = [int(ele) for ele in input().split()]
pairSum2(list2)
