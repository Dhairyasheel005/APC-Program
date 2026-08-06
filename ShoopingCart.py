cart = ["Milk", "Bread", "Rice"]

cart.append("Eggs")
cart.remove("Bread")

item = input("Search item: ")

if item in cart:
    print("Found")
else:
    print("Not Found")

print(cart)
print("Total items:", len(cart))