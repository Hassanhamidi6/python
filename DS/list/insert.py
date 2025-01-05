print(dir(list))

'''
insertion : insert append extend
'''
#mutable
li=[1,2,3,4,5]

#append
li.append(6)
print(li)

#insert
li.insert(4,"arham")
print(li)

#extend
l1=[1,2,3,4]
l2=[4,5,6,7]
l3=l1.extend(l2)
print(l1,l2)


#string immuatble
n="arham khan"
n+"hassan"
print(n)