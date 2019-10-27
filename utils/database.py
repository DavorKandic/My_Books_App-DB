from .database_connection import DatabaseConnection

"""
Concerned with storing and retrieving books from a database.
"""


def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
    


def take_input():
    inp = input('Your choice: ')
    return inp.lower().strip()
    


def add_book(name, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        """
        ***This way is DANGEROUS because of SQL injection ATTACK!***
        cursor.execute(f'INSERT INTO books VALUES("{name}","{author}",0)')
        """
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))
    
    print('Database updated!\n')
    
    
def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
    
        cursor.execute('SELECT * FROM books')
        # Creating a list of dictionaries that represent books.
        books = [{
            'name': row[0],
            'author': row[1],
            'read': row[2]
                  }
            for row in cursor.fetchall()]
        cursor.fetchall() # [(name, author, read),(name, author, read)] :::List of tuples
    
    return books
    
def mark_book_as_read(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
    
        cursor.execute('UPDATE books SET read=1 WHERE name=?',(name, ))
    
    print('Database updated!\n')
    

def delete_book(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
    
        cursor.execute('DELETE FROM books WHERE name=?',(name, ))
    
    print('Database updated!\n')
    
    