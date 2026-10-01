import pandas as pd

data = {
    "Rahul": 60000,
    "Priya": 45000,
    "Amit": 75000,
    "Sneha": 55000,
    "Rohit": 90000
}

s = pd.Series(data)

print("Employee Salary:")
print(s)

print("\nHighest Salary:")
print(s.max())

print("Lowest Salary:")
print(s.min())

print("Average Salary:")
print(s.mean())

print("\nEmployees earning more than 50000:")
print(s[s > 50000])