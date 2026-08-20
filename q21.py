employee1_skills = {"Python", "SQL", "Excel", "Java"}
employee2_skills = {"Java", "AWS", "SQL", "Docker"}
common_skills = employee1_skills & employee2_skills
unique_emp1 = employee1_skills - employee2_skills
unique_emp2 = employee2_skills - employee1_skills
all_skills = employee1_skills | employee2_skills
print("Common:", common_skills)
print("Unique to Employee 1:", unique_emp1)
print("Unique to Employee 2:", unique_emp2)
print("All skills:", all_skills)
