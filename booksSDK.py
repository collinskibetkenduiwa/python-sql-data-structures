import sqlite3
from book import Book
def cursor():
    return sqlite3.connect('books.db').cursor()
c=cursor()

c.execute('CREATE TABLE IF NOT EXISTS books(title TEXT,pages INTEGER)')

c.connection.close()

def add_book(book):
    c = cursor()
    with c.connection:
        c.execute("INSERT INTO books VALUES (?, ?)", (book.title, book.pages))
    c.connection.close()
    return c.lastrowid 

def get_books():
    c=cursor()
    books=[]
    with c.connection:
        for book in c.execute('SELECT * FROM books'):
            books.append(Book(book[0],book[1]))

    return books

def get_books_by_title(title):
    c=cursor()
    with c.connection:
        c.execute('SELECT * FROM books WHERE title=?',(title,))
    data= c.fetchone()

    if not data:
        return None

def update_book(book,new_title,new_pages):
    c=cursor()
    with c.connection:
        c.execute('UPDATE books SET title=?,pages=? WHERE title=? AND pages=?',(new_title,new_pages,book.title,book.pages))
    book=get_books_by_title(new_title)
    c.connection.close()
    return book

def delete_book(book):
    c=cursor()
    with c.connection:
        c.execute('DELETE FROM books WHERE title=? and pages=?',(book.title,book.pages))
    rows=c.rowcount
    c.connection.close
    return rows