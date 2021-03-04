import tkinter
from random import randint
from tkinter import messagebox
from tkinter import END
from book import Book 
import booksSDK


books=[]

def add_to_text():
    book=Book(title_entry.get(),pages_entry.get())

    booksSDK.add_book(book)
    listbox.insert(END,book)
    title_entry.delete(0,END)
    pages_entry.delete(0,END)
def remove_from_text():
    book_tuple=listbox.curselection() /0
    book=books.pop(book_tuple(0))
    if(booksSDK.delete_book(book)):
        listbox.delete(book_tuple)


tk=tkinter.Tk()

tk.title("Listbox")

listbox=tkinter.Listbox(tk)
listbox.pack()


for book in booksSDK.get_books():
    books.append(book)
    listbox.insert(END,book)


title=tkinter.Label(tk,text="Book Title")
title.pack()

title_entry=tkinter.Entry(tk)
title_entry.pack()

pages=tkinter.Label(tk,text="Book pages")
pages.pack()

pages_entry=tkinter.Entry(tk)
pages_entry.pack()

# pages_entry=tkinter.label(tk)
# pages_entry.pack()

button=tkinter.Button(tk,text="Add Value",command=add_to_text)
button.pack()
button=tkinter.Button(tk,text="Remove Value",command=remove_from_text)
button.pack()
tk.mainloop()

# listbox.insert(0,"Hello",'hi','yo')
# listbox.delete(0)

# low=0
# high=20

# rand=randint(low,high)
# print(rand)

# def check(guess):
#     if guess < rand:
#         tkinter.Label(tk,text=f"{guess} is too low").pack
#     elif guess  > rand:
#         tkinter.Label(tk,text=f"{guess} is too high").pack
#     else:
#         tkinter.messagebox.showinfo("YOU WIN",f"{guess} is correct")

# # print(randint(low,high))
# tk=tkinter.Tk()
# # tk.mainloop()

# tkinter.Label(tk,text="Gues a number {low} t0 {high}(inclusive)")

# entry=tkinter.Entry(tk)
# entry.pack()

# button=tkinter.Button(tk,text="Guess",command=lambda: check(int(entry.get())))
# button.pack()

# tk.mainloop()