
def maximumFrequency(list):

#for adding keys and its corresponding values to dict
    d = {}
    max = 0
    for i in list:
        d[i] = d.get(i,0) + 1
        if d[i] > max:
            max = d[i]

    for key in d:     #to check the key and its value
        if d[key] == max:
            return key

list1 = [int(ele) for ele in input().split()]
print(maximumFrequency(list1))


