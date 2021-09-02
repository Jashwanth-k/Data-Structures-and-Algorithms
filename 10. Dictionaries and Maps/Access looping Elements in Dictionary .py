#access elements in Dictionary

a = { 1:2, 3:4, 'list' : [1,2,3], 'dict' : {'b':'ball'} }
print(a)

print(a[1])

print(a.get('list'))
b = a.get(10,'absent')
print(b)

print(a.keys())
print(a.values())

print(a.items())
print()

for i in a:
    print(i)
print()

for i in a:
    print(i,a[i])
print()

for i in a.values():
    print(i)
print()

print('list' in a)
print('li' in a)

