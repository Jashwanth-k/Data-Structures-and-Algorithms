#T.C is O[n]
#S.C is O[d] depends on d

def rotate_array(a,d):
# temp stores the elements from 0 to d i.e [1,2]
    temp = a[:d]
    for i in range(len(a)-d):
        a[i] = a[i+d]
# depending up on d. elements indexes are changed
    a[len(a)-d:len(a)] = temp[:d]
# last part of list[a] i.e len(a)-d to len(a) is replaced by temp
    return a

a = [1,2,3,4,5,6]
d = 2
print(rotate_array(a,d))