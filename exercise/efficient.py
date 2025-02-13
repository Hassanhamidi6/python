'''
CSV -> comma separated files
similar to excel
.csv
'''

import pandas as pd
import os

# data={
#     "id":[1],
#     "name":["arham"],
#     "cnic":[4130340],
#     "batch":[2022],
#     "contact":["03003020"]
# }

# df=pd.DataFrame(data)
# print(df)
# print(df.shape)#it will tell the rows ad columns
# print(df.head(10))#it will print number of rows specified

path="exercise.py\\data.csv"

def Load_Data():
    if os.path.exists(path):
        df=pd.read_csv(path)
        return df
    else:
        data={
        "id":[],
        "name":[],
        "cnic":[],
        "batch":[],
        "contact":[]
         }
        df=pd.DataFrame(data)
        df.to_csv(path)
        return df

def insert():
    try:
        df=Load_Data()
        id=int(input("Enter the id"))
        if df[df.id == id].empty:
            name=input("Enter the name")
            contact=input("Enter the contact")
            cnic=input("Enter the cnic")
            batch=input("Enter the batch")

            data={
                   "id":[id],
                   "name":[name],
                   "cnic":[cnic],
                   "batch":[batch],
                   "contact":[contact]
                    }
            new_entry=pd.DataFrame(data)
            df=pd.concat([df,new_entry])
            df.to_csv(path,index=False)
        else:
            print("Duplicate ID")

    except Exception as e:
        raise e
    
def delete():
    try:
        df= Load_Data()
        id=int(input("Enter the id"))
        if df[df.id == id].empty:
            print("Data does not exist")
        else:
            df=df[df.id != id]
            df.to_csv(path,index=False)
    except Exception as e:
        raise e
    
def retrieve():
    df=Load_Data()
    print(df)

def retrieve_specific():
    df=Load_Data()
    id=int(input("Enter the id "))
    if df[df.id == id].empty:
        print("Data does not exist")
    else:
        print(df[df.id == id])

def filter_by_batch():
    batch=int(input("Enter the batch I will show you the data"))
    df=Load_Data()
    if df[df.batch == batch].empty:
        print("Data does not exist")
    else:
        print(df[df.batch == batch])
