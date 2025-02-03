'''
Class Mobile Phone 

attributes -> model , price , color , companyname

_repr_ 
function sare objects print
specific objects

@static method , True , False

def mob price increment by model name

class attributes , oppo , vivio

'''
class Mobile:
    iphone=30
    samsung=20
    redme=40
    all=[]

    def __init__(self,name , model , color, price):
        self.name=name
        self.model=model
        self.color=color
        self.price=price
        Mobile.all.append(self)
    
    def __repr__(self):
        return f"Mobile({self.name}, {self.model}, {self.color}, {self.price})"
    
    @classmethod
    def price_update(cls):
        updated_list=[]
        for element in cls.all:
            if element.name == "iphone":
                element.price+=cls.iphone
                updated_list.append(element)
            elif element.name == "redme":
                element.price+=cls.redme
                updated_list.append(element)
            elif element.name == "samsung":
                element.price+=cls.samsung
                updated_list.append(element)
        print(updated_list) 

mob1=Mobile(name="iphone", model="f11", color="black",price=300)
mob1=Mobile(name="redme", model="f11", color="black",price=300)

Mobile.price_update()

