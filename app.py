from utils import database as db


USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice:"""


db.create_book_table()

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()  
        elif user_input == 'd':
            prompt_delete_book()  
        else:
            print('Unknown input. Please, try again.')
                
        user_input = db.take_input()
                      
    
# def prompt_add_book() -> ask for book name and author
def prompt_add_book():
    book_name = input('Enter a name of a the book: ')
    book_author = input('Enter author\'s full name: ')
    db.add_book(book_name, book_author)


# def list_books() -> show all the books in our list
def list_books():
    books = db.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")
    
    
# def prompt_read_book() -> ask for book name and chage it to "read" in our list
def prompt_read_book():
    book_name = input('Enter a name of a the book: ')
    db.mark_book_as_read(book_name)
    
    
# def prompt_delete_book() -> ask for book name and remove book from list
def prompt_delete_book():
    book_name = input('Enter a name of the book: ')
    db.delete_book(book_name)

menu()
print('Bye-bye!')