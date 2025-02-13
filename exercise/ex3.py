student={
    "id":[],
    "name":[],
    "batch":[],
    "cnic":[],
    "contact":[]
}

def insert():
    id=int(input("Enter the id"))
    if id in student["id"]:
        print("ID alredy exist")
    else:
        name=input("Enter the name")
        batch=input("Enter the batch")
        cnic=int(input("Enter the cnic"))
        contact=int(input("Enter the contact"))

        student["id"].append(id)
        student["name"].append(name)
        student["batch"].append(batch)
        student["cnic"].append(cnic)
        student["contact"].append(contact)

def retrieve():
    print(student)

def delete():
    pass

def update():
    try:
        id=int(input("Enter the id"))
        if id in student["id"]:
            
    
    except Exception as e:
        print ("Error occurd")

def retrieve_specific():
    pass


interface='''
----------------Stuednt Management System------------------------
press 1, To insert the student data
press 2, To retrieve the student data 
press 3, To retreive specific student data
press 4, To update student data
press 5, To delete the student data
press 6, To exit
'''


while True:
    user_choice=int(input(interface))

    if user_choice==1:
        insert()
        continue

    if user_choice==2:
        retrieve()
        continue

    if user_choice==3:
        retrieve_specific()
        continue

    if user_choice==4:
        update()
        continue

    if user_choice==5:
        delete()
        continue

    else:
        print("Thankyou for using the applicaton")
        break
