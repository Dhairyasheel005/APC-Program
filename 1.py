import pandas as pd


data = {
    "Student ID": [101, 102, 103, 104, 105],
    "Student Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohit"],
    "Python Marks": [80, 65, 90, 72, 85],
    "DBMS Marks": [75, 70, 88, 68, 92],
    "Mathematics Marks": [85, 60, 95, 75, 80]
}


df = pd.DataFrame(data)


print("Student Data:")
print(df)


df["Total Marks"] = (
    df["Python Marks"] +
    df["DBMS Marks"] +
    df["Mathematics Marks"]
)


df["Average Marks"] = df["Total Marks"] / 3

print("\nDataFrame with Total and Average Marks:")
print(df)


print("\nStudents who scored more than 75% average:")
print(df[df["Average Marks"] > 75])