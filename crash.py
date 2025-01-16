'''
Define
l=[1,2,3,4]
elemnt access
l[2]
slicing
l[2:5]
methods
print(dir(list))

l.
functions
max(l),min(),sum(),type,len, rounde,t,c
for loop

if else
'''

#define
m={
    "id":[1,2,3],
    "name":["hassan","arham","ali"]
}

#accessingelemnts
l=m['id']

#methods
print(dir(dict))

b=m.copy()
m.clear()

print(b.items())
print(b.keys())
print(b.values())

for key,value in b.items():
    print(key,value)