import pandas as pd

data = {
    "Patient_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Riya", "Suresh", "Neha", "Raj"],
    "Age": [65, 45, 72, 30, 68],
    "Disease": ["Diabetes", "Fever", "Heart", "Cold", "Cancer"],
    "Medical_Charges": [60000, 20000, 90000, 15000, 75000]
}

df = pd.DataFrame(data)

print("Patients above 60:")
print(df[df["Age"] > 60])

print("\nAverage Medical Charge:")
print(df["Medical_Charges"].mean())

print("\nMaximum Medical Charge:")
print(df["Medical_Charges"].max())

print("\nPatients with charges greater than 50000:")
print(df[df["Medical_Charges"] > 50000])