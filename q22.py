available_books = {"Python Basics", "Data Structures", "Algorithms", "DBMS"}
requested_books = {"Algorithms", "Operating Systems", "DBMS"}
available_requested = requested_books & available_books
print(available_requested)
