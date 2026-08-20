student_dept = {"Aarav": "CSE", "Priya": "ECE", "Rahul": "CSE", "Meena": "Mech", "Kiran": "ECE"}
dept_groups = {}
for name, dept in student_dept.items():
    dept_groups.setdefault(dept, []).append(name)
print(dept_groups)
