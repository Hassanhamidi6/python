'''
command line student management application

---------------Problem Statement ------------
A institute named as Hiast is fed up with their manual work of student data management so they wanted to 
automate this process using python. They reached to us for create a command line application which allows 
them to manage student data efficiently.

---------------Requirements-------------------
Students credentials:
       --Student ID (unique for each student)
       --Student name
       --Batch
       --CNIC
       --Contact
--------Functionalities-------------------
A program will run automatically by running a single file

- User can insert the data of new student (registeration)
- User can delete the data of currently present student
- User can also update the data of currently present student except their ID
- User can retrieve the data of particular student by their ID
- User can retrieve the data of all student present 

Done this application with best practices ,
1.Implement  error handling using try except
2.User cannot insert the duplicate id it must be throrw error 
3.Use functional programming for each operation e.g Insertion, Deletion and so on
'''

interface='''
--------------------------------------------------------------
1,To insert the data 
2,To delete the data 
3,To update the data
4,To retrieve the data
5,To retrieve particular student data
6,To exit
---------------------------------------------------------------
'''

data={
    "id":[],
    "name":[],
    "batch":[],
    "cnic":[],
    "contact":[],
}


def insert():
    id=int(input("Enter the id to insert"))
    if id in data["id"]:
        print("ID already exist")
    else:
        name=input("Enter the name")
        batch=input("Enter th batch")
        cnic=int(input("Ebter the cnic"))
        contact=int(input("Enter the contact"))

        data["id"].append(id)
        data["name"].append(name)
        data["batch"].append(batch)
        data["cnic"].append(cnic)
        data["contact"].append(contact)

def delete():
    id=int(input("Enter the id to delete"))
    if id in data["id"]:
        index=data["id"].index(id)
        for keys in data:
            data[keys].pop(index)
    else:
        print("ID didnot exist")   

def retrieve_specific():
    id=int(input("Enter the id to retrieve specific data"))
    if id in data["id"]:
        index=data["id"].index(id)
        for keys in data:
          print(data[keys][index])
    else:
        print("ID did not exist")

def update():
    id=int(input("Enter the id to update"))
    if id in data["id"]:
        index=data["id"].index(id)
        name=input("Enter the name")
        batch=input("Enter the batch")
        cnic=int(input("Enter the cnic"))
        contact=int(input("Enter the conact"))

        data["name"][index]=name
        data["batch"][index]=batch
        data["cnic"][index]=cnic
        data["contact"][index]=contact
        print("Data updted successfully")
    else:
        print("ID didnot exist")


def retrieve():
    print(data)

insert()
insert()
retrieve()
update()
retrieve_specific()
delete()
retrieve()



