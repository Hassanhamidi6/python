input_params='''
-------------Welcome to the Software------------
Press 1, for the retrieve the data 
Press 2, for write the data 
press 3, for exit
------------------------------------------------
'''
while True:
    user_selection=int(input(input_params))

    customer_id=[1,2]
    customer_name=["Taimoor","Hassan"]
    product=["Laptop","Mobile"]
    product_price=[20,60]
    product_quantity=[4,2]
    total=[80,120]

    if user_selection == 1:
        print (f"CustomerID->{customer_id}\n CustomerName-> {customer_name}\n Product->{product}\n ProductPrice->{product_price}\n ProductQuantity->{product_quantity}\n Total->{total}")

    elif user_selection == 2:
        input_quantity=int(input("How many entrie you want to insert: "))
        for i in range (1,input_quantity+1):
            print(f" Enter {i} data")
            customerID=int(input("Enter Custoemr ID"))
            customerName=input("Enter Customer Name")
            ProductName=input("Enter the Product Name")
            ProductPrice=int(input("Enter the Prodcut Price"))
            ProductQuantity=int(input("Enter the product Quantity"))
            Totalprice=ProductPrice*ProductQuantity

            customer_id.append(customerID)
            customer_name.append(customerName)
            product.append(ProductName)
            product_price.append(ProductPrice)
            product_quantity.append(ProductQuantity)
            total.append(Totalprice)

            print("Data Entered Successfully")
            print (f"CustomerID->{customer_id}\n CustomerName-> {customer_name}\n Product->{product}\n ProductPrice->{product_price}\n ProductQuantity->{product_quantity}\n Total->{total}")




    else:
        print ("Thsnkyou for using the Application!!!")
        break