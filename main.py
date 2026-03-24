# Library 
import Regex_Library
from model import Books, Library

    
def main():
    library = Library("Book_name.txt")
    while True:
        choice = int(input("""Welcome to the Library 
                Pick an option
                  1. View list of books
                  2. Take a book
                  3. Donate a book 
                  4. Exit """))
        if choice == 1:
            library.book_list()

        elif choice == 2:    
            library.take_books()  

        elif choice == 3:
            book = get_books()
            library.donate_book(book)
            print("Book donated successfully ")
  

def get_books():
    name = input("Enter Book name ") 
    author = input("Enter the Author's name ") 
    genre = input("Enter the genre name ")    
    
    if not all([
        Regex_Library.valid_text(name),
        Regex_Library.valid_text(author),
        Regex_Library.valid_text(genre)
    ]):
        print("Invalid characters detected")
        return Books(name, author, genre)    



if __name__ == "__main__":
    main()