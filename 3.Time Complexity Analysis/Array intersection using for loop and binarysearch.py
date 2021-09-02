def binarySearch(a,x):
    a = sorted(a)
    si = 0
    ei = len(a)-1
    while si <= ei:
        mid = (si+ei)//2

        if a[mid] == x:
            return mid
        else:
            if a[mid] > x:
                ei = mid-1
            else:
                si = mid+1

a  = [2,3,4,6,8]
x = 5
a2 = [2,3,4,7]
for i in a2:
    if binarySearch(a,i) != None:
        print(i)