'''
Exercises by harshisht vashist 

of functions which are already define in python

Enumerate function 

Filer function 

Map function 

Zip function 



'''

name=["abc","hassan", "hamidi"]
# pos=0
# for i in name:
#     print(f"{pos} --> {i}")
#     pos+=1


# for pos,i in enumerate(name):
#     print(f"{pos}-->{i}")

def target(l,st):
    for pos,names in enumerate(l):
        if  names ==target:
            return pos
    return -1


print(target(name,"hassan"))

#hassan 