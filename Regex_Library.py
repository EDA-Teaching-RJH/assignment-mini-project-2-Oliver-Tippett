import re

def valid_text(text):
    pattern = r"^[A-Za-z0-9 ]+$"
    return bool(re.match(pattern, text))

def format_book(book):
    return f"{book.name} - {book.author} - {book.genre}"
