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
while True:
    user_selection=int(input(input_params))

    customer_id=[1,2]
    customer_name=["arham","hassan"]
    product=["panadol","brufen"]
    product_price=[10,20]
    product_quantity=[2,4]
    total=[20,80]

    if user_selection == 1:

        print(f"CustomerIDS-> {customer_id}\nCustomerName-> {customer_name}\nProduct-> {product}\nProductPrice-> {product_price}\nProductQuantity->{product_quantity}\nTotal->{total}")
    elif user_selection == 2:
        input_quantity=int(input("How many entries you want to insert : "))
        for i in range(1,input_quantity+1):
            print(f"Enter {i} data")
            customerid=int(input("Enter Customer ID"))
            customername=input("Enter Customer Name")
            productname=input("Enter product name")
            productprice=int(input("Enter product price"))
            productquantity=int(input("enter product quantity"))
            totalprice=productprice*productquantity

            customer_id.append(customerid)
            customer_name.append(customername)
            product.append(productname)
            product_price.append(productprice)
            product_quantity.append(productquantity)
            total.append(totalprice)
            
            print("Data Entered Succesfully")
            print(f"CustomerIDS-> {customer_id}\nCustomerName-> {customer_name}\nProduct-> {product}\nProductPrice-> {product_price}\nProductQuantity->{product_quantity}\nTotal->{total}")
    else:
        print("Thank you for using the application !!!")
        


