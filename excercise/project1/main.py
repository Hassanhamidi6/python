from utils import Utils
import os
import pandas as pd

dataset_path="excercise/project1/dataset.csv"
obj=Utils(dataset_path=dataset_path)

if os.path.exists(dataset_path):
    try:
        df=pd.read_csv(dataset_path)
    except Exception as e:
        print("No columns to parse")
else:
    df=pd.DataFrame(
        {
            "id":[],
            "name":[],
            "email":[],
            "contact":[],
            "batch":[]
        }
    )
    df.to_csv(dataset_path,index=False)



INTERFACE='''
Press 1 , to insert the data
Press 2 , to delete the data
Press 3 , to update the data
Press 4 , to retrieve the data
Press 5 , to retrieve specific data
Press 6 , to exit
'''

while True:
    user_choice=int(input(INTERFACE))
    if user_choice ==1:
        obj.insert()
    elif user_choice ==2:
        obj.delete()
    elif user_choice ==3:
        obj.update()
    elif user_choice ==4:
        obj.retrieve()
    elif user_choice ==5:
        obj.retrieve_specific()
    elif user_choice ==6:
        print("Thank you for using this application")
        break
    else:
        print("Not a valid Option")
        continue
    