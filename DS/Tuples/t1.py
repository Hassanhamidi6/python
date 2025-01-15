#defination
m=(1,2)

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
