import booksSDK
from book import Book

def print_menu():
    print("""Choose an option
    1.Print all books.
    2.add a book
    3.update a book
    4.delete a book  
    """)

while True:
    print_menu()
    response=int(input())
    if response == 1:
        books=booksSDK.get_books()
        for book in books:
            print(book)

    elif response ==2:
        print('What is the name of the book')
        title=input()
        print('How many pages is the book')
        pages=int(input())
        book=Book(title,pages)
        booksSDK.add_book(book)
    elif response ==3:
        print('What is the curent title')
        title=input()
        print('What is the current number of pages')
        pages=input()
        book=Book(title,pages)
        print('what is the new title')
        new_title=input()
        print('New number of pages')
        new_pages=input()
        booksSDK.update_book(book,new_title,new_pages)
    elif response ==4:
        print('Enter the title of the book to delete')
        title=input()
        print('Enter the number of pages')
        pages=input()

        book=Book(title,pages)
        print(booksSDK.delete_book(book)) 
    else:
        print('Thanks for your time,hope to see you again')
        break








# from book import Book
# import booksSDK

# book=Book('What the fuck is this caleb',56)

# # print(booksSDK.add_book(book))
# # print(booksSDK.get_books())
# print(booksSDK.get_books_by_title('What the fuck is this caleb'))