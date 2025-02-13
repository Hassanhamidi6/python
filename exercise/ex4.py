library={
    "id":[],
    "name":[],
    "price":[],
}

def insert ():
    try:
        id=int(input("Enter the id to insert"))
        if id in library["id"]:
            print ("Already exist")
        else:
            name=input("Enter the name")
            price=int(input("Enter the price"))
    except Exception as e:
        print("Error occurd")

    library["id"].append(id)
    library["name"].append(name)
    library["price"].append(price)

def delete():
    try:
        id=int(input("Enter the id to delete"))
        if id in library["id"]:
            index=library["id"].index(id)
            for keys in library:
                library[keys].pop(index)
        else:
            print("Given ID did not present")
    except Exception as e :
        print ("Error occurd")

def retrieve_specific():
    try:
        id=int(input("Enter the id to retrieve the data"))
        if id in library["id"]:
            pass
        else:
            print("Given ID does not exist")
    except Exception as e:
        print("Error occurd")

def update():
    id=int(input("Enter the id"))
    if id not in library["id"]:
        pass
    else:
        pass

def retrieve():
    print(library)

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
    if user_choice== 1:
        insert()
        continue
    elif user_choice==2 :
        retrieve()
        continue
    elif user_choice==3:
        retrieve_specific()
        continue
    elif user_choice==4:
        update()
        continue
    elif user_choice==5:
        delete()
        continue
    else :
        print ("Thankyou for using the application")
        break
