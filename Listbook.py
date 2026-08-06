books = ["Python", "Java", "C"]

books.append("HTML")

book = input("Search book: ")

if book in books:
    print("Available")

books.remove("Java")

print(books)
print("Total books:", len(books))