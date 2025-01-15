l=[1,2,3,4,5]
m=[]
for i in l:
    m.append(i**2)
print(m)

print([i**2 for i in l if i%2 != 0])

