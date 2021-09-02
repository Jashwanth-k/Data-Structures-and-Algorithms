# T.C is O[1]
def rotate_array(a,d):
# first totally reverse the list
    a = list(reversed(a))

# then seperate the list into two parts to understand.first part is 0 to n-d
# second part is n-d to n and now add those two lists. 'n' is len(list)

    a = list(reversed(a[:len(a)-d])) + list(reversed(a[len(a)-d:len(a)]))

    print(a)
a = [2,6,3,1,5,9,8]
d = 2
rotate_array(a,d)