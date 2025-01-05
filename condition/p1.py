# if condition:
#     body
# elif conditon:
#     body

# else:
#     body

'''
input name salary char
'''

# name,salary,char=input("Enter the data").split(' ')

# salary=int(salary)
# name=name.lower()
# char=char.lower()

# if name[0] == char:
#     salary20=(salary/100)*20
#     salary=salary+salary20
#     print(salary)
# else:
#     print(salary)

total=100
name,subject,marks_obtain=input("Enter the data\n").split(' ')
marks_obtain=int(marks_obtain)

percentage=(marks_obtain/total)*100

# if percentage >= 80:
#     print("A1")
# elif 70<=percentage<80:
#     print("A")

# elif 60<=percentage<70:
#     print("B")
# elif 50<=percentage<60:
#     print("C")
# else:
#     print("Fail")

grade = "A1" if percentage >=80 else "A" if 70<=percentage<80 else "B" if 60<=percentage<70 else "C" if  50<=percentage<60 else "Fail"

print(grade)




