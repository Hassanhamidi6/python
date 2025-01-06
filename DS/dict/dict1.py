'''
data structure
key value pairs
'''

#dictdefine
m={}
print(type(m))


#initializing dict
k={
    1:"arham",
    2:"hassan"
}

#accessing elements in dict
print(k[1])


#dictionary eng-urdu
meaning={
    "what":"kia",
    "why":"kyun",
    "who":"kon"
}
string=input("Enter the word i will tell you the meaning")
print(meaning[string])

#adding new element in dict
meaning["when"]="kab"
print(meaning)


#updating new element in dict
meaning["what"]="kia hua"
print(meaning)

