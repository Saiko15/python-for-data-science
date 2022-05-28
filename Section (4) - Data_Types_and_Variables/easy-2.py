name1 = str(input("Enter The First Student's Name: "))
id1 = int(input("Enter The First Student's ID: "))
grade1 = float(input("Enter The First Student's Grade: "))

name2 = str(input("Enter The Second Student's Name: "))
id2 = int(input("Enter The Second Student's ID: "))
grade2 = float(input("Enter The Second Student's Grade: "))

avg_grade = (grade1 + grade2) / 2

print('Information for students and their "math" grades \n' , name1 ,"(ID ", id1, ")", " got grade : ", grade1, "\n",  name2 ,"(ID ", id2, ")", " got grade : ", grade2, "\n", "Average math grade is ", avg_grade )