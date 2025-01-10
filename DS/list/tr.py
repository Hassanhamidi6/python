'''
Traversing: visiting each element single time
'''

FL=[1,2,3,4,5,6,7,8,9]

for counter in range(len(FL)):
    print(FL[counter])

for elements in FL:
    print(elements)


counter=0
while counter < len(FL):
    print(FL[counter])
    counter+=1

'''
Searching : Find 
'''

print(dir(list))

# m="arham"
# m.isupper()

m="hassan"

# for i in range(len(FL)):
#     if FL[i] == m:
#         print("True")
#     else:
#         print("False")

if m in FL:
    print("True")
else:
    print("false")