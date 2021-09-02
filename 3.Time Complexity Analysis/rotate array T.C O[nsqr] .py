#T.C is O[n*2]
def rotatory_array(a,d):
# should take a temporary variable temp and assigned with first element in list a[0]

    for i in range(d):
        temp = a[0]
        for j in range(len(a)-1):
            a[j] = a[j+1]
        a[len(a)-1] = temp

# after moving all the elements from left to right last element should
# be replaced with first element of list

    print(a)
a = [2,6,3,1,5,9,8]
d = 2
rotatory_array(a,d)

