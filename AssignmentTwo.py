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
        elif choice == "2":    
            books = get_books() #call get_books function
            print (f"Book: {books.name} | By: {books.author} | Genre: {books.genre}") 

def book_list():
    try:
        with open("Book_name.txt", "r") as file:
            lines = file.read()
            print (lines)
    except FileNotFoundError:
        print("Cant find file")

def get_books():
    name = input("Enter Book name ") 
    author = input("Enter the Author's name ") 
    genre = input("Enter the genre name ")    
    return Books(name,author,genre) #return to class

    


if __name__ == "__main__":
    main()