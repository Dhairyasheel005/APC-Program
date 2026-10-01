import pandas as pd

data = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Customer": ["Rahul", "Priya", "Amit", "Sneha", "Rohit"],
    "Product": ["Laptop", "Mobile", "TV", "Printer", "Tablet"],
    "Quantity": [2, 1, 2, 3, 2],
    "Price": [40000, 30000, 35000, 12000, 20000],
    "Discount": [2000, 1000, 3000, 500, 1500]
}

df = pd.DataFrame(data)

df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("All Orders:")
print(df)

print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])

print("\nHighest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("\nAverage Order Value:")
print(df["Final_Amount"].mean())