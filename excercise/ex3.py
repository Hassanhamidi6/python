'''

Exerces by harshisht vashist

Problem no 1, 
'''

name , age=input("Enter the name and age").split(" ")
age=int(age)
if age>=10 and (name[0]=="a" or name[0]=="A"):  
    print(f"{name} you can watch the movie")
else:
    print(f"{name} you are uner age")



# Problem no 2, give any number  as input and print sum of all numbers till that 
# for example given number is 5 so 1+2+3+4+5 


number=int(input("Enter any natural number "))
total=0
i=1
while i<=number:
    total+=i
    i+=1
print(total)

# Problem no 3, Take input and Ask user to print more than 1 digit , For example -->3456
# calculate the sum of numbers like     -->3+4+5+6  


num=input("Enter the numbers to get sum ")
total=0
i=0
while i<len(num):
    total +=int(num[i])
    i+=1
print(total)


# Problem no 4, Take input from user of his name and count the alphabets  

name=input("Enter the name: ")
i=0
temp=""                 #use not to repeat the character
while i<len(name):
    if name[i] not in temp:
        temp+=name[i]
        print(f"{name[i]} : {name.count(name[i])}")
        i+=1
   

# Problem no 4, same as problem no 3

name=input("Enter the name" )

for i in range(len(name)):
    print(f"{name[i]} : {name.count(name[i])}")


# Problem no 5, Guessing number game

import random 

winning_number=random.randint(1,100)
guess=1
while True:
    number=int(input("enter any number between 1 to 100: "))
    if number==winning_number:
        print(f"You won,you guess the number in {guess} times")
        break
    else:
        if number<winning_number:
            print("Too low")
        else:
            print("Too high")
