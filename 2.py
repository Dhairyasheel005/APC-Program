import pandas as pd


data = {
    "Employee ID": [101, 102, 103, 104, 105],
    "Employee Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohit"],
    "Department": ["IT", "HR", "Finance", "IT", "Marketing"],
    "Salary": [60000, 45000, 75000, 55000, 90000],
    "Experience": [3, 5, 8, 4, 10]
}


df = pd.DataFrame(data)

# Display DataFrame
print("Employee Data:")
print(df)


print("\nEmployees with salary greater than 50000:")
print(df[df["Salary"] > 50000])


average_salary = df["Salary"].mean()
print("\nAverage Salary:", average_salary)


highest_salary = df["Salary"].max()
print("Highest Salary:", highest_salary)


highest_experience = df.loc[df["Experience"].idxmax()]
print("\nEmployee with highest experience:")
print(highest_experience)