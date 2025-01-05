'''
String Class
'''

name='Hassan Mahmood'

print (type(name))

#title method

name_title=name.title()

#lower
name_lower=name.lower()

#upper
name_upper=name.upper()

#count

count_of_h=name.count('h')

#split
split_name_by_space=name.split(' ')

print(f"Original name is {name} the title of name is {name_title} the lower of name is {name_lower} the upper case of name is {name_upper}the count of char is {count_of_h} the split of name by space is {split_name_by_space} {type(name)}")


#string slicing

#name[ start: end: step]

# print(name[::2])
# print(name[::-1])

# var= "that charcter" if name == name[::-1] else "not that character"

# print(var)

#strip #rstrip #lstrip

print(name.strip())
print(name.rstrip())

name="          ar              "
print(name.lstrip())
print(name.rstrip())

'''
print 
str class
'''

