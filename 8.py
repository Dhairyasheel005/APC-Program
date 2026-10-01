import pandas as pd

data = {
    "Rahul": 80,
    "Priya": 72,
    "Amit": 90,
    "Sneha": 65,
    "Rohit": 85
}

s = pd.Series(data)

print("Series:")
print(s)

print("\nMarks of Amit:")
print(s["Amit"])

print("\nMaximum Marks:")
print(s.max())

print("Minimum Marks:")
print(s.min())

print("Average Marks:")
print(s.mean())

print("\nStudents scoring more than 75:")
print(s[s > 75])