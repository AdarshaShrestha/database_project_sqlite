from utils import database
import os

USER_CHOICE = """
Enter: 
- 'a' to add new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Please choose one: 
"""


def menu():
    database.create_book_table()
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
            print("Unknown command. Please use valid command.")

        user_input = input(USER_CHOICE)


# add new book in list
def prompt_add_book():
    name = input('Enter name of the new book: ')
    author = input('Enter author of the book: ')

    database.add_book(name, author)


# list all available books
def list_books():
    books = database.get_all_books()
    print("Here are your books.")
    for book in books:
        read = 'Yes' if book['read'] else 'No'
        print(f"{book['name']} by {book['author']}, read: {book['read']}")


# ask for book name and change it to "read" on books list
def prompt_read_book():
    name= input('Enter the name of the book you read: ')
    database.mark_book_as_read(name)
    print(f"The book, {name} has been updated to status: READ")


# ask book name and remove book from list
def prompt_delete_book():
    name = input('Enter the name of the book to delete from list: ')
    database.delete_book(name)
    print(f"{name} has been deleted from your book list.")


menu()



