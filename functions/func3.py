'''
Function -> parameter -> Limited -> Paramters == Arguments
'''

def LimParamFunctions(a:int,b:int,c:int)-> any:
    return a+b+c
print(LimParamFunctions(a=5,b=6,c=9))

# 1 - 1 , 2-2, 3-3 --- n-n

def Func(*arg) ->any:
    print(arg)

def KWordArgs(**kwargs) -> any:
    return kwargs

print(KWordArgs(name="arham",age=24,email="ak06598909@gmail.com"))

Func({1:2},{2:4},{5:6},{7:8})

# def ArgumentFunction(*args:int) -> int:
#     for i in args:
#         print(i)

# ArgumentFunction(10,20,30,40)

# *arg -> paramater , multiple arguments ->tuple
#      def m(*args):  
#          return args
#      m(str,int,list,tuple,dict)  -> tuple()   m(1,2,3,4,5)->(1,2,3,4,5) .m([],[],[]) ->([],[],[]) m({},{},{}) -> ({},{},{})
 
# **kwargs -> paramater . multiple key words arguments
#      def m(**kwargs):  
#         return kwargs
#     m(name="arham",,,,,,,) ->dictionary -> dict

# def Var(m:int,n="arham",*args,**kwargs):
#     print(f"Postional Arguments : {m}\nDefault Argument:{n}\nArgs:{args}\nkwargs:{kwargs}")

# Var(1,"arham",1,2,3,4,x=4,y=5)


'''
Args and Kwargs , and Paramter Precedence

'''