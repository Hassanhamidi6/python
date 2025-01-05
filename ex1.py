'''
Q1 write a python program which will tske string snd character as input 
and print count of that character in the string? if character is not in that string then print "character is not present"
'''

# name,char=input("Enter the name and the character you want to count ").split(' ')

# name=name.lower()
# char=char.lower()
# print(f"The char count of {char} in {name} is {name.count(char)}")


'''
Q2: write a python program which will take string as input
    and print all the character counts in that string
    arham 
      a: 2
      r:
      h
      a:2
'''

# string=input("Enter the string")

# name=""
# for char in string:
#     if char not in name:
#       print(f"{char} :{string.count(char)}")
#       name+=char

# str*int

# print("arham"*3)
'''
write a python program which will take a string as input and char as input

1.print name lower ,upper,title ,split by space
2.print count of that char in the string 
3.print all the character counts 
'''

string,char=input("enter the string and char you want to count").split(" ")

print (f"the lower of name is {string.lower()}\nthe upper of name is {string.upper()}\nthe title of name is {string.title()}")

name= "Hassan"
age= 20
gender="male"

print (f"this is the type of name {type(name)} this is the type of age{type(age)} this is the type gender{type(gender)}")