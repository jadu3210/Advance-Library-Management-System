def view_all_books(data):
    if data['all_books']:
        for book in data['all_books']:
            print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']} | Book Added At: {book['book_added_at']} | Book Last Updated At: {book['bookLast_update']}")
    else: print("No book found.")