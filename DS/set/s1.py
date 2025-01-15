'''
sets
'''
m={1,4,3,4,5}
print(m)

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


