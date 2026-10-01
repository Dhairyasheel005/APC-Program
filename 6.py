import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohit"],
    "Department": ["CSE", "CSE", "IT", "CSE", "IT"],
    "Total_Classes": [100, 100, 120, 100, 120],
    "Classes_Attended": [80, 70, 100, 60, 110]
}

df = pd.DataFrame(data)

df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print(df)

print("\nStudents with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])