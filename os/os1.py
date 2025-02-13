import os 

# print(dir(os))

'''
os.chdir()  -> change directory
os.getcwd() -> get current working directory
os.amkedirs() -> path -> folder create
os.path.ezists() -> check exist
os.path.join() -> do paths join kardeta hai
'''

#getcwd
current_dir=os.getcwd()
files=os.listdir(current_dir)

python_p=[]
pictures=[]
folders=[]

for i in files:                                               
    if not len(i.split('.')) == 1:
        if i.split('.')[1] == 'png':
            print(i)
            pictures.append(i)
        elif i.split('.')[1] == 'py':
            print(f"Python FIles : {i}")
            python_p.append(i)
    else:
        print(f"Folder{i}")
        folders.append(i)

print(python_p,pictures,folders)
os.chdir("E://")
new_dir=os.getcwd()