class Item:
    discount=20
    def __init__(self, name , price , quantity ):
        self.name=name
        self.price=price
        self.quantity=quantity


    def cal_price(self):
        return self.price*self.quantity
        
    @classmethod
    def is_integer (cls):
        cls.discount=30

print(Item.discount)
Item.is_integer()
print (Item.discount)
