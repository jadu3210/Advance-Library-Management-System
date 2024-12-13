from add_book import add_books
from view import view_all_books
from update_book_file import update_book
from remove import remove_book
from search import search_book
from borrow_book import lend_book, return_book
from save_all import*



def main():
    data = load_all_data()

    while True:
        print("\nWelcome to Library Management System")
        print("0. Exit")
        print("1. Add Books")
        print("2. View All Books")
        print("3. Book Update")
        print("4. Book Remove/Delete")
        print("5. Book Search")
        print("6. Lend Book")
        print("7. Return Book")

        menu = input("Select any option: ")

        if menu == "0":
            print("Thanks for using Library Management System")
            break
        elif menu == "1":
            data = add_books(data)
        elif menu == "2":
            view_all_books(data)
        elif menu == "3":
            data = update_book(data)
        elif menu == "4":
            data = remove_book(data)
        elif menu == "5":
            search_book(data)
        elif menu == "6":
            data = lend_book(data)
        elif menu == "7":
            data = return_book(data)
        else:
            print("Invalid option. Choose a right option.")

if __name__ == "__main__":
    main()
