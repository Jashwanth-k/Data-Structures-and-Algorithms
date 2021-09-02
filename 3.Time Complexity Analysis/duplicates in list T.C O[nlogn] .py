#time complexity of this solution is O[nlogn] 
def duplicates_list(a):
    a = sorted(a)
#instead of this sorted(A) line use mergesort or quicksort
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            print(a[i])


a = [0,7,2,5,4,7,1,3,6]
duplicates_list(a)