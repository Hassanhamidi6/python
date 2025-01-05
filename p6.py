'''
Operators
  --Arithmetic
       --+ ,-,/,*,//
  --comparision
       -- ><>=<=
  --assignment
    -- =, +=,-=,/=,*=
  --logical
       And or Not
  --increment decrement operator ++  -- 
'''

number1,number2 = input("Enter number 1 and number 2 ").split(' ')
number1,number2=int(number1),int(number2)
# print(f"{number1+number2} {number1-number2} {number1*number2} {number1/number2}")

if number1 >= number2:
    print("number1 is greater")
else:
    print("number2 is greater")

if  number1 >= number2 and  number2 > number1:
    print("yes")
else:
    print("no")





