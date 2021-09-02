def tower_honai(n,a,b,c):
    if n == 1:
        print('move 1st dick from',a,'to',c)
        return
    tower_honai(n-1,a,c,b)
    print('move',n,'th disk from',a,'to',c)
    tower_honai(n-1,b,a,c)

n = int(input('enter :'))
tower_honai(n,'s','h','d')