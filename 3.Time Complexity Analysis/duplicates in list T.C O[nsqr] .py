#the T.C is 0[n*2] because here we are using calculating the output by taking an
#element in list and comparing it with (n-1) elements i.e [n square]
def duplicates_list(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j:
                if a[i] == a[j]:
                    return a[i]

a = [0,7,2,5,4,7,1,3,6]
print(duplicates_list(a))