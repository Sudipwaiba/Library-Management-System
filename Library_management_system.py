# Library Management System => For Admins
# 1. Ask the user to visit or create the LMS
# IF create, ask name, location, etc and append the LMS into libraries
# If visit, ask name of library, check if exist or not, if exist, visit it, else not found 

# After visit:
# 1. Menu of LMS : Add book, remove book, withdraw book, view books
# 2. Seperate database/list for every LMS
# 3. Use loops functions and OOP concepts
lms_lists = []


class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price
        
class EBook(Book):
    def __init__(self,name, author, price, size):
        super().__init__(name, author, price)
        self.size = size
        
class LMS:
    # books = []
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
        
    def add_book(self,book):
        self.books.append(book)
        
    def remove_book(self):
        is_found = False
        book_name = input("Enter the book name to remove: ")
        for book in self.books:
            if book.name == book_name:
                self.books.remove(book)
                print("Book found and removed")
                is_found = True
        if not is_found:
            print("Book not found")
            
    def search_book(self):
        is_found = False
        book_name = input("Enter the book name to search: ")
        for book in self.books:
            if book.name == book_name:
                is_found = True
                index = self.books.index(book)
                print(f"{book_name} found at index {index}")
        if not is_found:
            print("Book not found")
            
    def view_books(self):
        for book in self.books:
            print(f"Book Name = {book.name}")
            print(f"Book Author = {book.author}")
            print(f"Book Price = {book.price}")
            if "EBook" in str(book):
                print(f"Book Size = {book.size}")
            
    
    
    
    
    
# b1 = Book("Parijaat","Jhamak Kumari Ghimire", 50)
# print(b1.name)
# print(b1.author)
# print(b1.price)

# eb1 = EBook("Munamadan","Laxmi Prasad Devkota",100,"10MB")
# print(eb1.name)
# print(eb1.author)
# print(eb1.price)
# print(eb1.size)


while True:
    vorc = input("Do you want to visit or create a LMS?(v/c). Enter e for exit : ")
    match vorc:
        case 'v':
            is_found = False 
            lms_name = input("Enter the name of lms to visit: ") 
            for lms in lms_lists:
                if lms.name == lms_name:
                    print("LMS visited")
                    is_found = True
                    while True:
                        choice = input("Enter 1 for add_book, 2 for remove_book, 3 for search_book, 4 for view_books, 5 for exit: ")
                        match choice:
                            case '1':
                                # add logic
                                books_count = int(input("ENter how many books you want to add:(in number): "))
                                for i in range(books_count):
                                    book_name = input("Enter book name")
                                    book_author = input("Enter book author")
                                    book_price = input("Enter book price")
                                    book_type = input("Enter the type, physical/online (p/o): ")
                                    match book_type:
                                        case 'p':
                                            book = Book(book_name, book_author, book_price)
                                            lms.add_book(book)
                                        case 'o':
                                            book_size = input("Enter book size: ")
                                            ebook = EBook(book_name, book_author, book_price, book_size)
                                            lms.add_book(ebook)
                                        case _:
                                            print("Invalid Input")
                            case '2':
                                # remove logic
                                lms.remove_book()
                            case '3':
                                # search logic
                                lms.search_book()
                            case '4':
                                # view logic
                                lms.view_books()
                            case '5':
                                print("Exiting")
                                break
                            case _:
                                print("Invalid Input")
            if not is_found:
                print("LMS not found")
        case 'c':
            name = input("ENter the name of the LMS: ")
            address = input("ENter the address of the LMS: ")
            lms = LMS(name, address)
            lms_lists.append(lms)
            print(lms_lists)
        case 'e':
            print("Exiting")
            break
        case _:
            print("Invalid Input")