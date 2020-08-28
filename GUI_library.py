from tkinter import *
import tkinter as tk
import sqlite3
from time import strftime


def create_table():
    con = sqlite3.connect('library.db')
    cursorobj = con.cursor()
    cursorobj.execute(
        "CREATE TABLE IF NOT EXISTS bookss(id INTEGER primary key AUTOINCREMENT,Title text,year int,Author text,ISBN int )")
    con.commit()
    print("table created")


##create_table()

def insert_data():
    con = sqlite3.connect('library.db')
    cursorobj = con.cursor()
    cursorobj.execute("INSERT INTO bookss(Title,year,Author,ISBN) VALUES('Half Girlfriend',2010,'Chetan Bhagat',100)")
    cursorobj.execute("INSERT INTO bookss(Title,year,Author,ISBN) VALUES('Electronics',2015,'ABC',101)")
    cursorobj.execute(
        "INSERT INTO bookss(Title,year,Author,ISBN) VALUES('Computer network',2011,'william stalings',102)")
    cursorobj.execute("INSERT INTO bookss(Title,year,Author,ISBN) VALUES('Two states',2009,'Chetan Bhagat',103)")
    cursorobj.execute("INSERT INTO bookss(Title,year,Author,ISBN) VALUES('Harry Potter',2010,'JK rowling',104)")
    con.commit()
    print("inserted")


##insert_data()


def delete_data():
    con = sqlite3.connect('library.db')
    cursorobj = con.cursor()
    cursorobj.execute("DELETE from bookss where id=24")
    con.commit()
    print("deleted")


##delete_data()
root = Tk()

root.geometry('630x300')

root.title("Book Library")


def select_data():
    con = sqlite3.connect('library.db')
    cursorobj = con.cursor()
    result = cursorobj.execute("SELECT id from bookss")
    n = 1
    label_one = Label(frame, bg="skyblue", height=20,
                      width=40)
    label_one.grid(row=3, columnspan=4)

    label_5 = Label(frame,
                    bg="skyblue",
                    height=12,
                    width=46)
    label_5.grid(row=3, columnspan=4)
    label1 = Label(label_one, text="Title", bg="skyblue", fg="black")
    label1.grid(row=1, column=1)

    label2 = Label(label_one, text="Year", bg="skyblue", fg="black")
    label2.grid(row=1, column=2)

    label3 = Label(label_one, text="Author", bg="skyblue", fg="black")
    label3.grid(row=1, column=3)

    label4 = Label(label_one, text="ISBN", bg="skyblue", fg="black")
    label4.grid(row=1, column=4)

    for row in result:
        label_1 = Label(label_one, text=row, bg="skyblue", anchor="ne")
        n = n + 1
        label_1.grid(row=n, column=0)

    result1 = cursorobj.execute("SELECT Title from bookss")
    n = 1
    for row in result1:
        label_1 = Label(label_one, text=row, bg="skyblue", anchor="ne")
        n = n + 1
        label_1.grid(row=n, column=1, sticky='W')

    result2 = cursorobj.execute("SELECT year from bookss")
    n = 1
    for row in result2:
        label_1 = Label(label_one, text=row, bg="skyblue", anchor="ne")
        n = n + 1
        label_1.grid(row=n, column=2)

    result3 = cursorobj.execute("SELECT Author from bookss")
    n = 1
    for row in result3:
        label_1 = Label(label_one, text=row, bg="skyblue", anchor="ne")
        n = n + 1
        label_1.grid(row=n, column=3, sticky='w')

    result4 = cursorobj.execute("SELECT ISBN from bookss")
    n = 1
    for row in result4:
        label_1 = Label(label_one, text=row, bg="skyblue", anchor="ne")
        n = n + 1
        label_1.grid(row=n, column=4)
    label_5.grid_remove()


def add_data():
    con = sqlite3.connect('library.db')
    cursorobj = con.cursor()
    a = data_1.get()
    b = data_2.get()
    c = data_3.get()
    d = data_4.get()
    cursorobj.execute('insert into bookss(Title,year,Author,ISBN) values (?,?,?,?)', (str(a), int(b), str(c), int(d)))
    con.commit()
    print('added')
    command = select_data()
    command = clear_text()


##def delete_data(id):
##    con=sqlite3.connect('library.db')
##    cursorobj=con.cursor()
##    cursorobj.delete(id=id)
##    con.commit()
##    print("data deleted successfuly")
##    command=select_data()

def search_data():
    con = sqlite3.connect('library.db')
    cursorobj = con.cursor()

    label_two = Label(frame, bg="skyblue", height=20, width=55)
    label_two.grid(row=3, columnspan=4)
    label_5 = Label(frame, bg="skyblue")
    label_5.grid(row=3, columnspan=4)

    cursorobj.execute("SELECT Title FROM bookss WHERE id = (?)", (data_id.get(),))
    cursorobj.execute("SELECT Title FROM bookss WHERE Author = (?)", (data_3.get(),))

    result = cursorobj.fetchone()
    n = 1
    for row in result:
        label_1 = Label(label_5, text="                        ", bg="skyblue")
        label_1.grid(row=1, column=1)
        label = Label(label_5)
        label.config(text=row, bg="skyblue")
        label.grid(row=1, column=1)

    cursorobj.execute("SELECT year FROM bookss WHERE id = (?)", (data_id.get(),))
    result = cursorobj.fetchone()
    n = 1
    for row in result:
        label_2 = Label(label_5, text="                        ", bg="skyblue")
        label_2.grid(row=1, column=2)
        label = Label(label_5)
        label.config(text=row, bg="skyblue")
        label.grid(row=1, column=2)

    cursorobj.execute("SELECT Author FROM bookss WHERE id = (?)", (data_id.get(),))
    result = cursorobj.fetchone()
    n = 1
    for row in result:
        label_3 = Label(label_5, text="                        ", bg="skyblue")
        label_3.grid(row=1, column=3)
        label = Label(label_5)
        label.config(text=row, bg="skyblue")
        label.grid(row=1, column=3)

    cursorobj.execute("SELECT ISBN FROM bookss WHERE id = (?)", (data_id.get(),))
    result = cursorobj.fetchone()
    n = 1
    for row in result:
        label_4 = Label(label_5, text="                        ", bg="skyblue")
        label_4.grid(row=1, column=4)
        label = Label(label_5)
        label.config(text=row, bg="skyblue")
        label.grid(row=1, column=4)

    command = clear_text()

    ##    title_text.set(result[1])
    ##    year_text.set(result[2])
    ##    author_text.set(result[3])
    ##    isbn_text.set(result[4])
    ##    data_id.configure(state='disabled')
    print('searched')
    con.commit()


def exit_data():
    root.destroy()


def clear_text():
    data_1.delete(0, 'end')
    data_2.delete(0, 'end')
    data_3.delete(0, 'end')
    data_4.delete(0, 'end')
    data_id.delete(0, 'end')


frame = Frame(root,
              bg="lightblue", height=40, width=70)
frame.grid(row=0, column=1)

label_one = Label(frame, bg="skyblue", height=20,
                  width=40)
label_one.grid(row=3, columnspan=4)

label_5 = Label(frame,
                bg="skyblue",
                height=12,
                width=46)
label_5.grid(row=3, columnspan=4)

label1 = Label(label_one, text="Title", bg="skyblue", fg="black")
label1.grid(row=1, column=1)

label2 = Label(label_one, text="Year", bg="skyblue", fg="black")
label2.grid(row=1, column=2)

label3 = Label(label_one, text="Author", bg="skyblue", fg="black")
label3.grid(row=1, column=3)

label4 = Label(label_one, text="ISBN", bg="skyblue", fg="black")
label4.grid(row=1, column=4)

label_title = Label(frame,
                    text="Title   ",
                    fg="black",
                    font="italian",
                    bg="lightblue",
                    anchor="ne")
label_title.grid(row=1, column=1)

title_text = StringVar()
data_1 = Entry(frame)
data_1.grid(row=1, column=2)

label_year = Label(frame,
                   text="Year   ",
                   fg="black",
                   font="italian",
                   bg="lightblue")
label_year.grid(row=2, column=1)

year_text = IntVar()
data_2 = Entry(frame)
data_2.grid(row=2, column=2)

label_author = Label(frame,
                     text="Author",
                     fg="black",
                     font="italian",
                     bg="lightblue")
label_author.grid(row=1, column=3)

author_text = StringVar()
data_3 = Entry(frame)
data_3.grid(row=1, column=4)

label_isbn = Label(frame,
                   text="ISBNO",
                   fg="black",
                   font="italian",
                   bg="lightblue")
label_isbn.grid(row=2, column=3)

isbn_text = IntVar()
data_4 = Entry(frame)
data_4.grid(row=2, column=4)

label_id = Label(frame,
                 text="id",
                 fg="black", font="italian", bg="lightblue")
label_id.grid(row=1, column=5)
id_text = IntVar()
data_id = Entry(frame)
data_id.grid(row=1, column=6)

button_1 = Button(frame,
                  text="View",
                  bg="skyblue", fg="black", font="italian", relief="sunken", command=select_data, borderwidth=3)
button_1.grid(row=2, column=5)
button_2 = Button(frame,
                  text="Delete",
                  bg="skyblue", fg="black", font="italian", relief="sunken", borderwidth=3)
button_2.grid(row=2, column=6)
button_3 = Button(frame,
                  text="Add",
                  bg="skyblue", fg="black", font="italian", relief="sunken", command=add_data, borderwidth=3)
button_3.grid(row=3, column=5)
button_4 = Button(frame,
                  text="Search",
                  bg="skyblue", fg="black", font="italian", relief="sunken", borderwidth=3, command=search_data)
button_4.grid(row=3, column=6)
button_5 = Button(frame,
                  text="close",
                  bg="skyblue", fg="black", font="italian", relief="sunken", borderwidth=3)
button_5.grid(row=4, column=5)
button_6 = Button(frame,
                  text="  exit  ",
                  bg="skyblue", fg="black", font="italian", relief="sunken", borderwidth=3, command=exit_data)
button_6.grid(row=4, column=6)

