'''
input function
'''

print("Enter your name")
name=input()
print("Enter your age")
age=input()
print("Enter your gender")
gender=input()

name=str(input("Enter your name\n"))
age=int(input("Enter your age\n"))
gender=str(input("Enter your gender\n"))

name,age,gender= input("Enter your name age and gender and give them by space").split('/')

'''
type sequences : 
'''

name="ar\nar"
print(name)