contacts = {"Ravi": "9876543210", "Meena": "9123456780"}

def add_contact(name, phone):
    contacts[name] = phone

def search_contact(name):
    return contacts.get(name, "Not found")

def update_contact(name, phone):
    if name in contacts:
        contacts[name] = phone

def delete_contact(name):
    if name in contacts:
        del contacts[name]

def display_contacts():
    print(contacts)

add_contact("Anil", "9988776655")
update_contact("Meena", "9000000000")
print(search_contact("Ravi"))
delete_contact("Anil")
display_contacts()
