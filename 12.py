import pandas as pd

data = {
    "Rahul": 85,
    "Priya": 72,
    "Amit": 95,
    "Sneha": 68,
    "Rohit": 91
}

s = pd.Series(data)

print("Attendance:")
print(s)

print("\nAverage Attendance:")
print(s.mean())

print("\nAttendance below 75:")
print(s[s < 75])

print("\nAttendance above 90:")
print(s[s > 90])

print("\nHighest Attendance:")
print(s.max())