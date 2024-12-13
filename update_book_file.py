from save_all import *
from datetime import *

def update_book(data):
    search_book = input("Enter book title to update: ")
    book_found = False
    for book in data['all_books']:
        if book['title'] == search_book:
            book_found = True
            print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']} | Book Added At: {book['book_added_at']} | Book Last Updated At: {book['bookLast_update']}")
            title = input("Enter new Book Title (Leave blank to keep unchanged): ")
            author = input("Enter new Author Name (Leave blank to keep unchanged): ")
            year = input("Enter new Publishing Year Number (Leave blank to keep unchanged): ")
            price = input("Enter new Book Price (Leave blank to keep unchanged): ")
            quantity = input("Enter new Quantity Number (Leave blank to keep unchanged): ")

            if title:
                book["title"] = title
            if author:
                book["author"] = author
            if year:
                book["year"] = int(year) if year else book["year"]
            if price:
                book["price"] = int(price) if price else book["price"]
            if quantity:
                book["quantity"] = int(quantity) if quantity else book["quantity"]

            book["bookLast_update"] = datetime.now().strftime('%d-%m-%Y %H:%M')

            save_all_data(data)
            print('Book updated successfully.')
            return data

    if not book_found:
        print('No book found.')

    return data
