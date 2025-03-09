'''
Exercises by Harshisht vashist

of FUNCTIONS
'''
# Exercise number 1, function to print last char of name

def last_char(name:str)->str:
    return name[-1]


print(last_char("hassan"))

# Exercise number 2, function of odd even checker number

def odd_even_checker(number:int)->int:
    if number%2==0:
        print("even number")
    if number%2!=0:
        print("odd number")

odd_even_checker(12)

# Exercise number 3, function returning boolean value (True or False)

def even_check(num:int)->bool:
    if num%2==0:
        return True
    else:
        return False
    
print(even_check(4))

# Exercise number 5, take two numbers as input and return which number is greater 

def large_num(number1:int, number2:int)->int:
    if number1>number2:
        return number1
    else:
        return number2

number1=input("Enter first number: ")
number2=input("Enter second number: ")
bigger=large_num(number1,number2)
print(f"{bigger} is greater number")

# Exercise number 6, palindrom function 

def is_pelindrom(word):
    reverse_word=word[::-1]
    if word==reverse_word:
        return True
    else:
        False

word=input("Enter any word: ")
print(is_pelindrom(word))

# Exercise number 7, function which takes a list of numbers and return square of them

def square(l:list)->list:
    square=[]
    for i in l:
        square.append(i**2)
    return square

print(square([1,2,3,4]))

# Exercise nummber8, function which returns reverse list

def reverse_list(ls:list)->list:
    ls.reverse()
    return ls
    
print(reverse_list([1,2,3,4]))

#Another method to do exercise number 8

def reverse_list(ls:list)->list:
    return ls[::-1]

print(reverse_list([1,2,3,4]))

# Another method of exercise 8

def reverse_list(l:list):
    r_list=[]
    for i in l:                                        #arham se pochna ha 
        popped_item=l.pop()
        r_list.append(popped_item)
    return r_list

print(reverse_list([1,2,3,4]))

#Exercise number 9, function which reverse list values

def reverse_values(l:list):
    ls=[]
    for i in l:
        ls.append(i[::-1])
    return ls

print(reverse_values(["abc","efg","xyz"]))

#Exercise number 10, function for makng odd even lists in one list
 
def filter_odd_even(l:list):
    even_list=[]
    odd_list=[]
    for i in l:
        if i %2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    output= [even_list, odd_list]
    return output

print(filter_odd_even([1,2,3,4,5,6]))


# Exercise number 11, function which takes 2 list  as input and give same list values as ouput 
# For example--> [1,2,3,4] [1,2,5,6] -->[1,2]

def common_element(l1:list, l2:list):
    l3=[]
    for i in l1:
        if i in l2:
            l3.append(i)
    return l3

print(common_element([1,2,3,4],[1,2,6,7]))

# Exercise number 12, Function which takes a number as input and return a dictionary whivh contain cubes 
# till that number , For example (3)--> {1:1, 2:8, 3:27}
            
def numbers_cube(num)->dict:
    d={}
    for i in range(1,num+1):
        d[i]=i**3
    return d
print(numbers_cube(3))

#Exercise number13, make a dictionary which will take your name , age , favorite movie and favorite song as an input


dict={}

name=input("Enter the name: ")
age =input("Enter the age: ")
fav_movie=input("Enter the favorite movies seperated by comma : ").split(",")
fav_songs=input("Enter the favorite songs seperated by comma: ").split(",")

dict["name"]=name
dict["age"]=age
dict["fav_movies"]=fav_movie
dict["fav_songs"]=fav_songs

for keys,values in dict.items():
    print(f"{keys} : {values}")


# Exercise number 14, Using list comprehension 
# make a Function which takes list as an input and retrun reverse values

def reverse_string(l:list):
    ls=[]
    for i in l:
        ls.append(i[::-1])
    return ls

print(reverse_string(["abc","xyz"]))

# Another method , by using list comprehenion 

def reverse_str(l:list):
    return[i[::-1] for i in l]

print(reverse_str(["abc","efg","xyz"]))

#Exercise number 15, function take input a list and return if the type is int or float 

def type_checker(l:list):
    ls=[]
    for i in l:
        if type(i)==int or type(i)== float:
            ls.append(i)
    return ls

print(type_checker([True, False, 1, 6, [1,2,3], 0.9]))

#Another method by using list comprehension

def typ_check(l):

    return [str(i) for i in l if (type(i)==int or type(i)==float)]

print(typ_check([1,2.3,5,[1,2,3],True]))


#exercise number 16,function take input a number using *args and return the power of the given numbers in list

def to_power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        print("you didn't pass any args")

print(to_power(3,*[2,3,4]))


