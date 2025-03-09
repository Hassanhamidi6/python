import pandas as pd
class Utils:
    '''
    A python class which will be responsible for
    the functionality of my project
    '''
    def __init__(self,dataset_path):
        self.dataset_path=dataset_path

    def insert(self):
        df=pd.read_csv(self.dataset_path)
        id=int(input("Enter the id\n"))
        ids=df.id.tolist()
        if id in ids:
            print("Duplicate Id")
        else:
            email=input("Enter the email\n")
            batch=input("Enter the batch\n")
            contact=input("Enter the contact\n")
            name=input("Enter the name\n")
            temp=pd.DataFrame(
                    {
                "id":[id],
                "name":[name],
                "email":[email],
                "contact":[contact],
                "batch":[batch]
            }
            )
            final=pd.concat([df,temp])
            final.to_csv(self.dataset_path,index=False)
            print("Data Inserted Successfully")

    def delete(self):
        df=pd.read_csv(self.dataset_path)
        id=int(input("Enter the id you want to delete"))
        ids=df.id.tolist()
        if id in ids:
            df=df[df.id != id]
            df.to_csv(self.dataset_path,index=False)
            print("Data deleted successfully")
        else:
            print("ID does not exist")

    def update(self):
        df=pd.read_csv(self.dataset_path)
        id=int(input("Enter the ID you want to update\n"))
        ids=df.id.tolist()
        if id in ids:
            name=input("Enter the name\n")
            bacth=input("Enter the batch\n")
            contact=input("Enter the contact\n")
            email=input("Enter the email\n")
            df.loc[df.id == id,['name','batch','email','contact']]=[name,bacth,contact,email]
            df.to_csv(self.dataset_path,index=False)
            print("Data Updated successfully")
        else:
            print("ID does not exist")

    def retrieve(self):
        df=pd.read_csv(self.dataset_path)
        print(df)

    def retrieve_specific(self):
        df=pd.read_csv(self.dataset_path)
        id=int(input("Enter the id\n"))
        ids=df.id.tolist()
        if id in ids:
            specific=df[df.id == id]
            print(specific)
        else:
            print("ID not found")
