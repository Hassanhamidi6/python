'''
Student 
   id,name,marks,subject ->object attribute
   ,total_marks

   function -> instance method
   percentage -calculate 

   function -> jitne available objects print -> __repr__ -> class method
   function -> instance -> specific object 

   function -> instance method , marks update 
   function -> class method -> total marks update

'''

class Student:
    total_marks=100
    All=[]
    def __init__(self, name, id ,marks , subject):
        assert id>=0 ,f"error occurd"
        assert marks>=0 ,f"error occurd"
        self.name=name
        self.id=id
        self.marks=marks
        self.subject=subject
        Student.All.append(self)
    
    def __repr__(self):
        return f"Student({self.name}, {self.id}, {self.marks}, {self.subject})"
    
    @classmethod
    def total_marks_update(cls, value, increment=True, decrement=False):
        if increment:
            cls.total_marks=cls.total_marks+value
        elif decrement:
            cls.total_marks=cls.total_marks-value
    
    def percentage(self):
        return (self.marks/Student.total_marks)*100
    
    def specific_object(self):
        print(self.id,self.name,self.marks,self.subject)

    def marks_update(self,value,increment=True,decrement=False):
        if increment:
            self.marks=self.marks+value
        elif decrement:
            self.marks =self.marks - value
  
std1=Student(name="arham",id=1,marks=40,subject="math")
std2=Student(name="hassan",id=2,marks=70,subject="eng")
std3=Student(name="Ali",id=3,marks=90,subject="urdu")


print(std1.marks)

std1.marks_update(value=20,increment=True,decrement=False)
print(std1.marks)
print(Student.All)

print(Student.total_marks)
Student.total_marks_update(value=20)
print(Student.total_marks)

print(Student.All)

# class Mobile :
#     iphone= 40
#     samsung= 60
#     redme= 30
#     all=[]

#     def __init__(self,name, model, color, price  ):
#         self.name=name
#         self.model=model
#         self.color=color
#         self.price=price 
#         Mobile.all.append(self)

#     def __repr__(self):
#         return f"Mobile({self.name},{self.model},{self.color},{self.price})"
    
#     def specific_objects(self):
#         print(self.name , self.model , self.color , self.price)

    
# mob1=Mobile(name="iphone",model="iphone15", color="black", price=500)