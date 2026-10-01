import pandas as pd

data = {
    "P101": 65,
    "P102": 45,
    "P103": 72,
    "P104": 30,
    "P105": 68
}

s = pd.Series(data)

print("Patient Ages:")
print(s)

print("\nAverage Age:")
print(s.mean())

print("\nOldest Patient:")
print(s.idxmax(), s.max())

print("\nYoungest Patient:")
print(s.idxmin(), s.min())

print("\nPatients above 60:")
print(s[s > 60])