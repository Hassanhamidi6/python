'''
1: write a python program which contains a dictionary with following keys and values
          ID: [values],
          name: [values],
          salaries: [values]
          marks: [values]
 then I want some analysis on this data , 
    a. Highest salary person 
    b. Lowest salary person
    c. Average salary gving to employes
    d. Highest percentage
    e. Lowest percentage
    f. Average of marks
    g. Calculate Median of salary or marks if possible
'''
# program for all above things

d={
    "id": [0,1,2,3,4],
    "name": ["Hassan", "Arham", "Taimoor", "Ali", "Rahdain"],
    "salaries": [6001,9400,56000,2456,9887],
    "marks": [90,50,80,60,40]
}
# max(d["salaries"])                 
# highest_salary_person=d["salaries"].index(max(d["salaries"]))
# lowest_salary_person=d["salaries"].index(min(d["salaries"]))
# print(f"The name of person is {d['name'][lowest_salary_person]} and ID is {d['id'][lowest_salary_person]}")

max_salary=max(d["salaries"])
min_salary=min(d["salaries"])
highest_salary_person= d["salaries"].index(max(d["salaries"]))
lowest_salary_person=d["salaries"].index(min(d["salaries"]))
w=sum(d["salaries"]) 
k=len(d["salaries"])
Average=(w/k) 

percentage=[]
for i in d["marks"] :
    print (i)
    a=round((i/150)*100,2)

    percentage.append(a)

print(percentage) 

max_per=max(percentage)
min_per=min(percentage)

sum_marks=sum(d["marks"])
len_marks=len(d["marks"])
average_marks=sum_marks/len_marks

for keys in d:
    r=d[keys][highest_salary_person]
    print (r)

for keys in d:
    r=d[keys][lowest_salary_person]
    print(r)

print(f"{Average}, {max_per}, {min_per},{average_marks}")