import pandas as pd

data = {
    "Product": ["Laptop", "Mobile", "Laptop", "Tablet", "Mobile"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Electronics"],
    "Sales": [50000, 30000, 60000, 20000, 40000]
}

df = pd.DataFrame(data)

print("Sales Data:")
print(df)

product_sales = df.groupby("Product")["Sales"].sum()

highest_product = product_sales.idxmax()
highest_sales = product_sales.max()

print("\nHighest Selling Product:")
print(highest_product)
print("Total Sales:", highest_sales)

category_sales = df.groupby("Category")["Sales"].sum()

print("\nTotal Sales by Category:")
print(category_sales)