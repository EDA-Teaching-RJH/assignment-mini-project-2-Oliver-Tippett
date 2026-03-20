# Library 
import LibrariesofFunctions

class Books:   
    def __init__(self,name,author,genre):
        self.name = name
        self.author = author
        self.genre = genre
    
def main():
    while True:
        choice = int(input("""Welcome to the Library 
                Pick an option
                  1. View list of books
                  2. Take a book
                  3. Return a book
                  4. Donate a book 
                  5. Exit """))
        if choice == 1:
            book_list()

        elif choice == 2:    
            take_books() #call get_books function 

        elif choice == 4:
            book = get_books()
            donateBooks = donate_books(book)
            print("Book donated successfully ")

def book_list():
    try:
        with open("Book_name.txt", "r") as file:
            lines = file.read()
            print (lines)
    except FileNotFoundError:
        print("Cant find file")

def take_books():
    book_name = input("Enter the name of the book you want to take: ").lower() #Convert input to all lowercase
    try:
        with open("Book_name.txt", "r") as file: 
            books = file.readlines()
        
        found = False # Book not found yet 

        with open("Book_name.txt", "w") as file: 
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
    

def get_books():
    name = input("Enter Book name ") 
    author = input("Enter the Author's name ") 
    genre = input("Enter the genre name ")    
    return Books(name,author,genre) #return to class

def donate_books(book):
    with open("Book_name.txt", "a") as file:
        file.write(f"{book.name} - {book.author} - {book.genre}\n")

if __name__ == "__main__":
    main()