'''
Function: set of instructions which perform particular task
Function: input ----> [Function] -----> Output
Advantages: Code Reusability
Functional Programming
'''

#camel case writing

#function define

def Add(a,b):
    c=a+b
    
# a=Add(4,5)
# print(a)


def hassan(h:int,n:int) -> int :
    k=n+h
    return k

hassan(n=4,h=5)

def Square(num:int) ->int:
    return num**2


l=[1,2,3,4,6,7]
print([Square(i) for i in l])

def Percentage(obtain_marks:int):
    total=150
    per=round((obtain_marks/total)*100,2)
    return per


print(Percentage(obtain_marks=100))

def reverse(my_list:list) ->list:
    return my_list[::-1]

print(reverse(my_list=[1,2,3,4,5,6]))

def concatenate(first:str,second:str) -> str:
    return f"{first} {second}"

print(concatenate(first="arham",second="khan"))


def upper(st:str) ->str:
    a=st.upper()
    return a


total=150

def percentage(ob:int) -> float:
    per=(ob/total)*100
    return per

def form(l:list):
    for i in l:
       print(i)

