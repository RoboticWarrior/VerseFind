import os
import tkinter
import re

app = tkinter.Tk()
app.title('VerseFind')
app.state('zoomed')

def clear(home=False):
    for item in app.winfo_children():
        item.place_forget()

    if not home:
        home_button.place(relx=0.05, rely=0.05, anchor='center')

def home():
    clear(home=True)
    search_button.place(relx=0.5, rely=0.4, anchor='center')
    read_button.place(relx=0.5, rely=0.6, anchor='center')

def search_page():
    clear()
    search_widgets.input_box.place(relx=0.5, rely=0.5, anchor='center')
    search_widgets.enter_button.place(relx=0.5, rely=0.6, anchor='center')

def search():
    books = ('Matthew.txt', 'Mark.txt', 'Luke.txt')
    search_input = search_widgets.input_box.get()
    search_widgets.input_box.delete(first=0, last=tkinter.END)

    for book in books:
        book_open = open(book, 'r')
        book_read = book_open.readlines()
        book_open.close()
        write_out = open(f'{book[:-4]}_out.txt', 'w')

        for line in book_read:
            if ':' in line:
                line = line.strip(':')

            write_out.write()

home_button = tkinter.Button(app, text='🏠', font=('Arial', 30), fg='white', bg='green', command=home)

search_button = tkinter.Button(app, text='Search', font=('Arial', 30), fg='white', bg='blue', command=search_page)
read_button = tkinter.Button(app, text='Read', font=('Arial', 30), fg='white', bg='green')

class search_widgets:
    input_box = tkinter.Entry(app, width=20, font=('Arial', 30))
    enter_button = tkinter.Button(app, text='Enter', font=('Arial', 30), fg='white', bg='green')

class read:
    input_box = tkinter.Entry(app, width=20, font=('Arial', 30))
    enter_button = tkinter.Button(app, text='Enter', font=('Arial', 30), fg='white', bg='green', command=search)

home()

app.mainloop()