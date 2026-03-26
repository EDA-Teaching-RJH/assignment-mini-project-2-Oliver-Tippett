import re  #import regular expression

def valid_text(text):
    pattern = r"^[A-Za-z0-9 ]+$"  # ^ is start of string then A - Z , a - z , 0 - 9 , space , are allowed characters
                                  # + is one or more allowed characters then $ is end of string
    return bool(re.match(pattern, text))
    # re.match checks if the text matches the pattern
    # bool converts result into True or False
def format_book(book):
    return f"{book.name} - {book.author} - {book.genre}"
