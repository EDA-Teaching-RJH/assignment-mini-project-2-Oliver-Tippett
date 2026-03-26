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
                lines = file.read() # reads Book_name.txt file  
                print (lines) # prints the whole file
        except FileNotFoundError: 
            print("Cant find file") 

    def take_books(self):
        book_name = input("Enter the name of the book you want to take: ").lower() #Convert input to all lowercase
        try:
            with open(self.Book_name, "r") as file:  #open file in read mode
                books = file.readlines() 
        
            found = False # Track if book is found or not 

            with open(self.Book_name, "w") as file:  #open file in write mode
                for book in books:
                    name, author, genre = book.strip().split(" - ")  

                    if name.lower() == book_name and not found:     #if book is found
                        print(f"You took: {name} | {author} | {genre}") 
                        found = True
                        continue

                    file.write(book)  #write remaining books back into file

            if not found:
                print("This book was not found ")

        except FileNotFoundError:  # if file cant be found prevent crashing
            print("Book file not found")
    
    def donate_book(self, book):
        with open(self.Book_name, "a") as file: #open file in append so book added at end
            file.write(f"{book.name} - {book.author} - {book.genre}\n")