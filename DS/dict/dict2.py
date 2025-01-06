print(dir(dict))

meaning={
    "what":"kia",
    "why":"kyun",
    "who":"kon"
}

for key in meaning:
    print(key)

#keys
print(meaning.keys())
for keys in meaning.keys():
    print(keys)
#values
print(meaning.values())
for values in meaning.values():
    print(values)

#items
print(meaning.items())
for key,value in meaning.items():
    print(key,values)

for keys in meaning:
    print(f"{keys} is correspond to {meaning[keys]}")


for key,value in meaning.items():
    print(f"{key} correspond to {value}")