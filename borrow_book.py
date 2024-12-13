from datetime import *
from save_all import *

def lend_book(data):
    borrower_name = input("Enter borrower's name: ")
    phone_number = input("Enter borrower's phone number: ")
    book_title = input("Enter book title to lend: ")
    return_due_date = (datetime.now() + timedelta(days=7)).strftime("%d-%m-%Y")
    book_found = False
    for book in data['all_books']:
        if book['title'] == book_title:
            book_found = True
            if book['quantity'] > 0:
                book['quantity'] -= 1
                lend_entry = {
                    "borrower_name": borrower_name, "phone_number": phone_number, "book_title": book_title, "return_due_date": return_due_date }
                data['lend_info'].append(lend_entry)
                save_all_data(data)
                print(f"Book lent to {borrower_name}. Return due date is {return_due_date}.")
                return data
            else:
                print("There are not enough books available to lend.")
                return data
    if not book_found:
        print('Book not found.')
    return data
def return_book(data):
    book_title = input("Enter book title to return: ")
    borrower_name = input("Enter borrower's name: ")
    lend_found = False
    for entry in data['lend_info']:
        if entry['book_title'] == book_title and entry['borrower_name'] == borrower_name:
            lend_found = True
            data['lend_info'].remove(entry)
            for book in data['all_books']:
                if book['title'] == book_title:
                    book['quantity'] += 1
                    save_all_data(data)
                    print(f"Book returned by {borrower_name}.")
                    return data
    if not lend_found:
        print('Lend information not found.')
        return data