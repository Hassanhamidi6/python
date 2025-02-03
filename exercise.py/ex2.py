student={
    "id":[],
    "name":[],
    "cnic":[],
    "batch":[],
    "contact":[]
}


def insert():
    id=int(input("Enter the id"))
    if id in student["id"]:
        print("Duplicated id")
    else:
        
        name=input("Enter the name")
        cnic=int(input("Enter the cnic"))
        batch=input("Enter the batch")
        contact=int(input("Enter the contact"))

        student["id"].append(id)
        student["name"].append(name)
        student["cnic"].append(cnic)
        student["batch"].append(batch)
        student["contact"].append(contact)
        


def delete():
    try:
        id=int(input("Etner the id"))
        if id in student["id"]:
            index=student["id"].index(id)
            for keys in student:
                student[keys].pop(index)
        else:
            print ("The student with corresponding id does not exist")
    except Exception as e:
        raise e
def retrieve():
    print (student)    

def retrieve_specific():
    try:
        id=int(input("Enter the id. I'll retrieve the data"))
        index=student["id"].index(id)
        if id in student["id"]:
            for key in student:
                print(student[key][index])
        else:
            print("ID does not exist")

    except Exception as e:
        raise e

def update():
    try:
        id=int(input("Enter the id"))
        if id in student["id"]:
            index=student["id"].index(id)
            name=input("Enter the name")
            cnic=int(input("Enter the cnic"))
            batch=input("Enter the batch")
            contact=int(input("Enter the contact"))
            student['name'][index]=name
            student['cnic'][index]=cnic
            student['batch'][index]=batch
            student['contact'][index]=contact
            print("Data updated sucessfully")
        else:
            print("ID doesnot exist")
    except Exception as e:
        raise e
    



interface='''
------------------------Student Management System-----------------------------
Press 1, to register the new student
Press 2, to check the current data
Press 3, to retrieve specific student credentials
Press 4, to update the existing data
Press 5, to delete the data
Press 6, to Exit
-------------------------------------------------------------------------------
'''

while True:
    user_choice=int(input(interface))
    if user_choice == 1:
        insert()
        continue
    if user_choice == 2:
        retrieve()
        continue
    if user_choice == 3:
        retrieve_specific()
        continue
    if user_choice == 4:
        update()
        continue
    if user_choice == 5:
        delete()
        continue
    else:
        print("Thank you for using the application")
        break