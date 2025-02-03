import tkinter as tk
from tkinter import *
from tkinter import ttk

class Calculator:
    def __init__(self,root):
        self.root=root
        self.root.title("Calculator")
        self.root.geometry("500x500+400+100")

        self.frame=Frame(self.root,bg="yellow",border=5,relief=GROOVE)
        self.frame.pack(fill=BOTH,expand=True)

        self.text=Text(self.frame,font=("times new roman",20,"bold"),border=5,relief=RIDGE)
        self.text.place(x=0,y=0,width=490,height=70)

        self.create_button(text="1",x=0,y=75,command=None)
        self.create_button(text="2",x=110,y=75,command=None)
        self.create_button(text="3",x=190,y=75,command=None)
        self.create_button(text="+",x=270,y=75,command=None)
    
    def create_button(self,text,x,y,command):
        btn=Button(self.frame,text=text,bg="orange",fg="black",command=command,font=("times new roman",20,"bold"),activebackground="orange",activeforeground="black")
        btn.place(x=x,y=y,width=100,height=70)




if __name__ == "__main__":
    root=Tk()
    obj=Calculator(root=root)
    root.mainloop()


