#method 1
rows,colums = 4,4
arr = [[0 for i in range(colums)]for j in range(rows)]

arr[0][0] = 1

for i in arr:
    print(i)

#method 2
rows,colums = 4,4
arr = [[0]*colums]*rows

arr[0][0] = 1

for i in arr:
    print(i)

#for difference observe the output
