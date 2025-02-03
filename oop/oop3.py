class Item:
    discount_rate=0.8 #class level attribute
    all=[]
    def __init__(self, name , price , quantity ):
        assert price >=0
        assert quantity>=0

        self.name=name 
        self.price=price 
        self.quantity=quantity

        # Actions to execute 
        Item.all.append(self)

    def calprice(self):
        return self.price*self.quantity
    
    def discount(self):
        self.price=self.price*self.discount_rate

    def __repr__(self): # good practice for printing the instances
        return f"Item ('{self.name}', '{self.price}', '{self.quantity})"        
    

item1= Item(name="laptop", price =200 , quantity=4)
item2= Item(name="mobie", price =400 , quantity=3)
item3= Item(name="mouse", price =600 , quantity=4)
item4= Item(name="keyboard", price =1000 , quantity=2)

# print(item1.price)
# item1.discount()
# print (item1.price)

#To print names of instances 
# print (Item.all)
# for instance in Item.all:
#     print (instance.name)



# def table(a:int):
#     for i in range(1,11):
#         print (f"{i} x {a} = {i*a}")

# number=int(input("Enter the number\n"))
# table(number)