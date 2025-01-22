'''
Problem#1 : Dictionary -- key:value , Function -- dictionary as a parameter 
Key square , value cube , new dictionary

Problem2: Python func , Dictionary , 2 List , first list -- keys , second list --values

Probelm3: Python func -- > Number , sum(of all numbers)

Problem4: List --> Multiple list , [[1,2,3],[4,5,6]], square 

problem5: Func , ek number , us number ka table print 

Problem6: Write a function which will take number as input and print febonacci series until that number 
'''

def fabonacci(num:int):
    
    '''
    1 1 2 3 5 8
    '''
    a=1
    b=1
    l=[]
    l.append(a)
    l.append(b)
    for i in range(num):
      c=a+b
      l.append(c)
      a=b
      b=c
    return l


a=fabonacci(10)
print(a)
# Print -> Func -> Print( parameter) -> Terminal Display -> Print - func  , class , outside of func or class func() print(" ") func()
# Return -> Keyword -> Function <- Input -> output -> Return -> Func call -> input -> output -> return a= func(1,b) 


dic={
    1:4,
    2:5,
    3:9
}


# def SqOfKeys(dic:dict)->dict:
#     # d={}
#     # for keys,values in dic.items():
#     #     d[keys**2]=values**3
#     d={key**2:value**3 for key,value in dic.items()}
#     return d

# m=SqOfKeys(dic=dic)
# print(m)

# Input ->[Function] -> return -> parameters
m=5
def prob(d:dict)-> any:
  m=[]
  n=[]
  for keys,values in d.items():
    m.append(keys)
    n.append(values)
  return m,n

m=prob(d={1:2,2:3})
print(m)





def sum(d="hassan"):
  print(d)
sum(d="arham")

def Sort(lis:list,ascending:bool =True ,descending:bool=False):
  if ascending:
    m=[]
    for i in range(len(lis)):
      m.append(lis.pop(max(lis)))
    return m
  
  elif descending:
    m=[]
    for i in range(len(lis)):
      m.append(lis.pop(min(lis)))
    return m


# problem no.3

def sum(k:int)->int:
  r=0
  for i in range(1,k+1):
    r+=i
  return r


h=sum(k=12)
print(h)



def table(t:int)->int:
  
  for i in range(1,11):
    print(f"{t} x {i} = {t*i}")



table(6)
# n,m=(1,2) #value unpacking

# print(n,m)



l=[[1,2,3],[4,5,6],[15,16,17]]

# m=[]
# for i in l:
#   for k in i:
#     m.append(k**2)

m=[k**2  for i in l for k in i ]

print (m) 


# j=[]
# for i in l:                    
#   j.append([k**2 for k in i])

# print(j)

u=[[k**2 for k in i] for i in l]
print (u)


# def BinarySearch(l:list, num:int)->int:
#   start=0
#   End=len(l)
#   for i in range(len(l)):
#     mid=(start+End)//2

#     if l[mid] > num:
#       start=0
#       end=mid
#       mid=(start+end)//2

    
#     elif l[mid] <num:
#       start=mid
#       mid=(start+End)//2
    

#     elif l[mid] == num:
#       print(mid)
#     else:
#       print(-1)

# BinarySearch([1,2,3,4],3)
