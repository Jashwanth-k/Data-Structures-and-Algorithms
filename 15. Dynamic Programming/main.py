

def coin_change(values,V,i=0):

    if V == 0:
        return 1

    if i == len(values):
        return 0

    if V - values[i] >= 0:
        ans1 = coin_change(values,V-values[i],i+1)
        ans2 = coin_change(values,V,i+1)
        ans = ans1 + ans2
    else:
        ans = coin_change(values,V,i+1)

    return ans


values = [1,2,3]
V = 4
print(coin_change(values,V))
