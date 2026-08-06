students = ["Amit","Rahul","Priya"]

print("Total:", len(students))

name = input("Search student: ")

if name in students:
    print("Present")

students.append("Riya")
students.remove("Rahul")

print(students)