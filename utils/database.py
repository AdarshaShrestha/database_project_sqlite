import json
import sqlite3
import os
from .database_connection import DatabaseConnection

"""
Storing and retrieving books from a d json file

[
    {
        'name': 'Enlightment Now',
        'author': 'Steven Pinker',
        'read': True
    }
]
"""

# books_file = 'books.json'


def create_book_table():
    with DatabaseConnection('data.db') as connection:
        # connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

    #connection.commit()
    #connection.close()

    """with open(books_file, 'w') as file:
        json.dump([], file)"""


def add_book(name, author):

    with DatabaseConnection('data.db') as connection:
        #connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('INSERT OR IGNORE INTO books VALUES(?, ?, 0)', (name, author)) # to insert new books in the db or else ignore if the book is already in list

        #connection.commit()
        #connection.close()
    """books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)"""


def mark_book_as_read(name):
    with DatabaseConnection('data.db') as connection:
        #connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))

    #connection.commit()
    #connection.close()
    """books = get_all_books()

    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_all_books(books)"""


def get_all_books():
    with DatabaseConnection('data.db') as connection:
        #connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]       # [(name, author, read), (name, author, read).....]

    #connection.close()

    return books

    """with open(books_file, 'r') as file:
        return json.load(file)"""


"""def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)"""


def delete_book(name):
    with DatabaseConnection('data.db') as connection:

        #connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=?', (name,))

    #connection.commit()
    #connection.close()
    """books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)"""


