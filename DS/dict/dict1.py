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

# print(k["a"])

meaning={
    "what":"kia",
    "why":"kyun",
    "who":"kon"
}

string=input("Enter the word i will tell you the meaning")
print(meaning[string])

meaning["what"]="kab"
print(meaning)
print(dir(dict))

