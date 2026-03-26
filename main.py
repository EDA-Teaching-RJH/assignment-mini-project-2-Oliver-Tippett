# Library 
import Regex_Library
from Library_Functions import Books, Library

def get_books():
    name = input("Enter Book name ") 
    author = input("Enter the Author's name ")  #get book information 
    genre = input("Enter the genre name ")    
    
    if not all([
        Regex_Library.valid_text(name),
        Regex_Library.valid_text(author),  #checks inputs are valid 
        Regex_Library.valid_text(genre)
    ]):
        print("Invalid characters detected") #if not valid
        return    
    
    return Books(name, author, genre) #if valid

    
def main():
    library = Library("Book_name.txt")
    while True:  #infinite loop keep user in menu until they exit
        choice = int(input("""Welcome to the Library 
                Pick an option
                  1. View list of books
                  2. Take a book
                  3. Donate a book 
                  4. Exit """))
        if choice == 1:
            library.book_list()  #show all books

        elif choice == 2:    
            library.take_books()   #remove a book from library

        elif choice == 3:
            book = get_books()   #check new book is valid
            if book:
                library.donate_book(book)  #adds a book to library
                print("Book donated successfully ")
        
        elif choice == 4:  #end code
            break

if __name__ == "__main__":
    main()