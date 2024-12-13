from save_all import *
from datetime import *
from random import *


def add_books(data):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    while True:
        try:
            year = int(input("Enter Publishing Year Number: "))
            price = int(input("Enter Book Price: "))
            quantity = int(input("Enter Quantity Number: "))
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    isbn = randint(1000, 10000)
    book_added_at = datetime.now().strftime("%d-%m-%Y %H:%M")

    book = {
        "title": title,
        "author": author,
        "year": year,
        "price": price,
        "quantity": quantity,
        "isbn": isbn,
        "book_added_at": book_added_at,
        "bookLast_update": ''
    }
    data['all_books'].append(book)
    save_all_data(data)
    print("Book added successfully.")
    return data