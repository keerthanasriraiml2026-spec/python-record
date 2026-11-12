# Student Record Management with List, Tuple, Dictionary and CSV user
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("Enter student details:", i + 1)

    roll = input("Enter RollNo: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    mark = int(input("Enter Mark: "))

    student = {
        "RollNo": roll,
        "Name": name,
        "Department": dept,
        "Mark": mark
    }

    students.append(student)