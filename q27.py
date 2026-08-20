products_27 = {"Pen": 100, "Notebook": 5, "Bag": 20, "Bottle": 3, "Pencil": 8}

def add_product(name, qty):
    products_27[name] = qty

def update_quantity(name, qty):
    if name in products_27:
        products_27[name] = qty

def delete_product(name):
    if name in products_27:
        del products_27[name]

def search_product(name):
    return products_27.get(name, "Not found")

def low_stock():
    return {name: qty for name, qty in products_27.items() if qty < 10}

add_product("Eraser", 50)
update_quantity("Bag", 25)
print(search_product("Pen"))
print(low_stock())
delete_product("Bottle")
print(products_27)
