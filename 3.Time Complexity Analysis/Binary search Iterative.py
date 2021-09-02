def binarySearch(a,x):
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

a  = [1,2,3,4,5]
x = 5
print(binarySearch(a,x))