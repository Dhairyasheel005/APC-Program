import pandas as pd

data = {
    "Laptop": 50000,
    "Mobile": 30000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000
}

s = pd.Series(data)

print("Products and Prices:")
print(s)

# Increase every price by 10%
s = s * 1.10

print("\nPrices after 10% increase:")
print(s)

print("\nMost expensive product:")
print(s.idxmax(), s.max())

print("\nProducts costing more than 1000:")
print(s[s > 1000])