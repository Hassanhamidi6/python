'''
customer name , customer id , productbuy productprice productquantity total
read write exit

retrieve all the data
write , input and save sort 
exit
'''

input_params='''
---------------Welcome To the Software ----------------
Press 1, For retrieve the data
Press 2, For input the data
Press 3, For Exit
-------------------------------------------------------
'''
import pandas as pd
data={
   "id":[1,2,3,4],
   "name":["hassan","arham","taimoor","ali"],
   "marks":[40,50,60,70]
}

df=pd.DataFrame(data)

while True:
   user_choice=int(input(input_params))

   if user_choice == 1:
      print(df)
   elif user_choice == 2:
      num_entries=int(input("Enter how many entries you want to insert"))
      for entries in range(1,num_entries+1):
         print(f"Taking {entries} data")

         id=int(input("Enter the ID"))
         name=(input("Enter the name"))
         marks=int(input("Enter the marks"))

         data['id'].append(id)
         data['name'].append(name)
         data['marks'].append(marks)
         df=pd.DataFrame(data)
         print(df)
   else:
      print(f"{'-'*50}\n\tThank you for using the Application\n{'-'*50}")
      break



