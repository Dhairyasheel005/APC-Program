students_set = {"Aarav", "Priya", "Rahul", "Meena"}
name = input("Enter a name: ")
if name in students_set:
    print(name, "exists")
else:
    print(name, "does not exist")
