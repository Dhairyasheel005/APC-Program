books = {"B101": "Python Basics", "B102": "Data Structures"}

def add_book(book_id, name):
    books[book_id] = name

def search_book(book_id):
    return books.get(book_id, "Not found")

def remove_book(book_id):
    if book_id in books:
        del books[book_id]

def display_books():
    print(books)

def count_books():
    return len(books)

add_book("B103", "Algorithms")
print(search_book("B101"))
remove_book("B102")
display_books()
print("Total books:", count_books())
