from save_all import*
def remove_book(data):
    search_book = input("Enter book title to remove: ")
    book_found = False
    for book in data['all_books']:
        if book['title'] == search_book:
            book_found = True
            data['all_books'].remove(book)
            save_all_data(data)
            print('Book removed successfully.')
            return data
    if not book_found:
        print('No book found.')

    return data
