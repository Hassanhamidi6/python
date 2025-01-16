'''
sets
'''
m={1,4,3,4,5}
print(m)

#accessing elemnts
# print(m[0]) #slicing not allowed

print(dir(set))

k={13,14}
n={9,3}

n.add(13)
print (n)

print (k.difference(n,m))



m.discard(4)
print (m)    

#loop with sets
for i in m:
    print(i) 

l=[1,1,1,2,2,2,3,3,3]

l=list(set(l))

#sets are not subscriptable, not allow slicing
print(sum(m))
print(min(m))
print(max(m))
print(len(m))




print(n.issubset(m))
print(m.issuperset(k))
print(m.union(k))
print(m.intersection(k))
print(m.difference())


for i in m:
    if i > 50:
        print("greater")
    else:
        print("lower")

min , max, sum

m={1,2,3,4,5,6}
max(m)
