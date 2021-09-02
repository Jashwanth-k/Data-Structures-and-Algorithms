def unique_element(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j:  # if i==j i.e 1==1 same element called
                if a[i] == a[j]:
                    break  #breaks when same element found
            if j == len(a)-1:   #if j == last element index i.e not found
                print(a[i])

a = [2,3,1,6,3,6,2]
unique_element(a)