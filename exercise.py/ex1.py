'''
command line student management application

---------------Problem Statement ------------
A institute named as Hiast is fed up with their manual work of student data management so they wanted to 
automate this process using python. They reached to us for create a command line application which allows 
them to manage student data efficiently.

---------------Requirements-------------------
Students credentials:
       --Student ID (unique for each student)
       --Student name
       --Batch
       --CNIC
       --Contact
--------Functionalities-------------------
A program will run automatically by running a single file

- User can insert the data of new student (registeration)
- User can delete the data of currently present student
- User can also update the data of currently present student except their ID
- User can retrieve the data of particular student by their ID
- User can retrieve the data of all student present 

Done this application with best practices ,
1.Implement  error handling using try except
2.User cannot insert the duplicate id it must be throrw error 
3.Use functional programming for each operation e.g Insertion, Deletion and so on
'''

interface='''
--------------------------------------------------------------
1,To insert the data 
2,To delete the data 
3,To uodate the data
4,To retrieve the data
5,To retrieve particular student data
6,To retrieve the data of al students
---------------------------------------------------------------
'''
