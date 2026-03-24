class Books:   
    def __init__(self,name,author,genre):
        self.name = name
        self.author = author
        self.genre = genre

class Library:

    def __init__(self, Book_name):
        self.Book_name = Book_name

    def book_list(self):
        try:
            with open(self.Book_name, "r") as file:
                lines = file.read()
                print (lines)
        except FileNotFoundError:
            print("Cant find file")

    def take_books(self):
        book_name = input("Enter the name of the book you want to take: ").lower() #Convert input to all lowercase
        try:
            with open(self.Book_name, "r") as file: 
                books = file.readlines()
        
            found = False # Book not found yet 

            with open(self.Book_name, "w") as file: 
                for book in books:
                    name, author, genre = book.strip().split(" - ")

                    if name.lower() == book_name and not found:
                        print(f"You took: {name} | {author} | {genre}")
                        found = True
                        continue

                    file.write(book)

            if not found:
                print("This book was not found ")

        except FileNotFoundError:
            print("Book file not found")
    
    def donate_book(self, book):
        with open(self.Book_name, "a") as file:
            file.write(f"{book.name} - {book.author} - {book.genre}\n")