salaries = {"Ravi": 45000, "Kiran": 62000, "Meena": 38000, "Suresh": 75000}
top_earner = max(salaries, key=salaries.get)
low_earner = min(salaries, key=salaries.get)
avg_salary = sum(salaries.values()) / len(salaries)
above_50k = {name: sal for name, sal in salaries.items() if sal > 50000}
print("Highest:", top_earner, salaries[top_earner])
print("Lowest:", low_earner, salaries[low_earner])
print("Average:", avg_salary)
print("Above 50000:", above_50k)
