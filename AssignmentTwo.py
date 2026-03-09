# Library 

class Books:
    def __init__(self,name,author,genre):
        self.name = name
        self.author = author
        self.genre = genre
    
def main():
    books = get_books()
    print (f"Book: {books.name} | By: {books.author} | Genre: {books.genre}")

def get_books():
    name = input("Enter Book name ") 
    author = input("Enter the Author's name ") 
    genre = input("Enter the genre name ")
    return Books(name,author,genre)

    


if __name__ == "__main__":
    main()