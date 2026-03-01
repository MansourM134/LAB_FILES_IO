import Library.Librarian as Librarian

def main():
    library = {}
    
    menu = '''
    1 - add a book
    2 - remove a book
    3 - check out a book
    4 - return a book 
    5 - display all books 
    6 - exit
    '''

    while True:
        user_input = input(menu)
        if user_input == "1":
            title = input("enter the title of the book:")
            isbn = input("enter the isbn of the book: ")
            author = input("enter the author of the book: ")
            Librarian.add_book(library, title, isbn, author)

        elif user_input == "2":
            title = input("enter the title of the book: ")
            isbn = input("enter the ISBN of the book: ")
            Librarian.remove_book(library, title, isbn)

        elif user_input == "3":
            title = input("enter the title of the book: ")
            isbn = input("enter the ISBN of the book: ")
            Librarian.check_out_book(library, title, isbn)

        elif user_input == "4":
            title = input("enter the title of the book: ")
            isbn = input("enter the ISBN of the book: ")
            Librarian.return_book(library, title, isbn)
        
        elif user_input == "5":
            Librarian.display_books()
            

        elif user_input == "6":

            return False



main()
