name_list=[]
email_list=[]
subject_list=[]
marks_list=[]
percentage=[]
total_marks=100

for i in range(0,3):
   name,email,subject,marks =input("Enter student name , email, subject and marks (split by space)\n").split(" ")
   marks=int(marks)
   percent=(marks/total_marks) *100
   percentage.append(percent)
   name_list.append(name)
   email_list.append(email)
   subject_list.append(subject)
   marks_list.append(marks)

print(f"student_name : {name_list}\nstudent_email : {email_list}\nstudent_subject : {subject_list}\nstudent_marks : {marks_list}\npercentage : {percentage}")

