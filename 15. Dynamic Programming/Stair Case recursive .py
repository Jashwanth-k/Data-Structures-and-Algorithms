

def stair_case(m):

    if m == 0 or m == 1:
        return 1

    ans1 = stair_case(m-1)

    ans2 = stair_case(m-2)

    return (ans1 + ans2)

m = int(input())
print(stair_case(m))
