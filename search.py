def search_book(data):
    search_books= input("Enter book title to search: ")
    book_found = False
    for book in data['all_books']:
        if book['title'] == search_books:
            book_found = True
            print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']} | Book Added At: {book['book_added_at']} | Book Last Updated At: {book['bookLast_update']}")
            return data
    if not book_found:
        print('No book found.')