'''
basics of functions
'''

# Parameters vs arguments

def Arham(a,b,c):
    l=5
    print(type(a),type(b),type(c))
    return a+b+c

'''
Function Defination best approach
'''

def Sort(list_to_be_sort:list)-> list:
    '''
    This is the python Function which 
    takes input as a list 
    return a sorted list as output
    '''
    try:
        return  list_to_be_sort.sort()
    except Exception as e:
        print("This is an error")
    

'''
Function Call -> best approach
'''
l=[1,2,3,4,5]
m=[10,9,8,7]
Sort(list_to_be_sort=(2,3,4,5))



def string(s:str)-> str:
    """
    This function is taking parametres as a string 
    It will give print the string and return none
    """
    print(s)

string(s="Hassu")


def OddEvenChecker(l:list)->list:
    pass

