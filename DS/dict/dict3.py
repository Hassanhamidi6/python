# print(dir(dict))

# d={
#     1:"arham",
#     2:"hassan"
# }

# #clear -> dict mutable
# d.clear()
# print(d)

# #copy
# d={
#     1:"arham",
#     2:"hassan"
# }
# m=d.copy()
# print(m)

# #fromkeys
# n={}

# l=n.fromkeys([1,2,3],0)
# print(l)

# k=m.fromkeys(m.keys(),0)
# print(k)

# #pop
# m.pop(1)
# print(m)

# #popitem
# print(d.popitem())

# meaning={
#     "what":"kia",
#     "why":"kyun",
#     "who":"kon"
# }

# print(meaning.popitem())

# #setdefault
# meaning.setdefault("whom")
# print(meaning)

# #update
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 20, 'c': 30}

# dict1.update(dict2)
# print(dict1)

# #get
# print(meaning.get("what"))

# d={
#     "id":[1,2],
#     "name":["hassan","arham"]
# }
# import pandas as pd

# df=pd.DataFrame(d)
# df.to_csv("data.csv",index=False)

# print(dir(df))
# list
# number=int(input("enter the of which you want the table"))
# for i in  range(1,11):
#     print(f"{number} x {i} = {number*i}")

# num=int(input("Enter any number"))
# # h=0
# # for i in range (1,num+1):
# #      h=h+i

# print(sum([i for i in range(1,num+1)]))
    


# d={
#     "name":["Hassan","Taimoor","Arham"],
#     "id" : [6,8,2],
#     "age" :[20,21,22]
# }
# print(d.values())

# import time

# print(time.time())
# for i in d.values():
#     print(i[::-1])
# print(time.time())
# for key in d.keys():
#     print(d[key][::-1])
# print(time.time())
# for key,values in d.items():
#     print(values[::-1])
# print(time.time())
# for key in d:
#     print(d[key][::-1])

# enter the number:
# 5

# [1,4,9,16,25,36]
import math
number=int(input("Enter the number"))

l=[]
for i in range (1,number+1):
    l.append(math.sqrt(i))
print(l)    
