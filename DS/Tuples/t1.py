'''
Tuples 
Tuples are immuteable -->not changeable
Tuples can store any type of data type
we cannot change (add or delete) values from tuple once it created
but if there is list  inside the tuple we can use list methiods inside the tuple 
 
'''


#defination
m=(1,2,5)

#accessing elements
print(m[0])

#type
print(type(m))

#methods
print(dir(tuple))

print(m.count(1))
print(m.index(2))

#functions
print(sum(m))
print(min(m))
print(max(m))
print(len(m))
#aggregate functions
#if else with tuple
#loop with tuples
for i in m:
    if i >1:
        print("greater")
    else:
        print("lesser")
