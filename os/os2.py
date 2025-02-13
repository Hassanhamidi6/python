import os

root=os.getcwd()
folder_name="python_course"
new_folder_path=os.path.join(root,folder_name)

folders_list=["oop","functions","ds","loop","files","ifelse"]

for folders in folders_list:
    path=os.path.join(new_folder_path,folders)
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print("Folder already exists")

if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)    
else:
    print("Folder already exists")



