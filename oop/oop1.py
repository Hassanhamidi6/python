'''
how too create class 
how to crete objects 
how to initialize instance attributes 

Instance --> means objects

Magic methods 

assert--> use to make any value greater than 0 " assert price >= 0 "and also we can print customize error by giving fstring 

class attributes 
Instace attributes 
'''

class Item:
    discount_rate=0.8  #class level attribute 
    def __init__(self, name:str , price:int , quantity:int):
        
        assert price >= 0 , f"price shoulde be rgeater than 0"
        assert quantity >= 0 , f"quantity shoulde be rgeater than 0"

        self.name=name 
        self.price=price 
        self.quantity=quantity
    
    def calprice(self):
        return self.price*self.quantity
    def discount(self):
        self.price= self.price* self.discount_rate


item1=Item("laptop", 200, 5)
# item1.discount=20
print (item1.name , item1.price , item1.quantity , item1.calprice())
item1.discount()
print(item1.price)

item2=Item("mobile", 100, 2)
item2.discount_rate=0.6 # instance level attribute
item2.discount()
print (item2.price )