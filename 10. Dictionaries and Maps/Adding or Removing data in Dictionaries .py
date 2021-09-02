
a = { 1:2, 3:4, 'list':[1,2,3], 'dict':{4:5} }
print(a)

#for adding
a['tuple'] = (6,7,8)
print(a)

#for updating
a[1] = 10
print(a)

b = { 3:5, 'the':4, 2:100 }
a.update(b)
print(a)

#for deleting
a.pop('tuple')
print(a)

del a[1]
print(a)

a.clear()

print(a)
