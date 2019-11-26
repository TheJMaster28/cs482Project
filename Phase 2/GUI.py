import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import DatabaseConnector as db
import HelloWorld as hw
m = tk.Tk()


def toString(string):
    s = ""
    for i in string:
        for k in i:
            s += str(k)
            s += ", "
        s += "\n"
    return s


def app():
    global m
    frame1 = tk.Frame(m).grid()
    tk.Label(frame1, text="Path to File for Single Insert").grid(row=0)
    insert = tk.Entry(frame1)
    insert.grid(row=0, column=1)

    def doInsert():
        db.singlePlayersInsert(insert.get())

    button = tk.Button(frame1, text="Submit", command=doInsert)
    button.grid(row=0, column=2)

    # ---------------------------------------------------------------

    tk.Label(m, text="Path to File for Multi Insert").grid(row=1)
    Minsert = tk.Entry(frame1)
    Minsert.grid(row=1, column=1)
    Mtable = tk.Entry(frame1)
    tk.Label(frame1, text="Table to insert to").grid(row=1, column=2)
    Mtable.grid(row=1, column=3)

    def doMInsert():
        db.multInsert(Minsert.get(), Mtable.get())

    button = tk.Button(frame1, text="Submit", command=doMInsert)
    button.grid(row=1, column=4)

    # ----------------------------------------------------------------

    tk.Label(m, text="Path to File for Load Data Insert").grid(row=2)
    Linsert = tk.Entry(frame1)
    Linsert.grid(row=2, column=1)
    Ltable = tk.Entry(m)
    tk.Label(frame1, text="Table to insert to").grid(row=2, column=2)
    Ltable.grid(row=2, column=3)

    def doLInsert():
        db.loadData(Minsert.get(), Ltable.get())

    button = tk.Button(frame1, text="Submit", command=doLInsert)
    button.grid(row=2, column=4)

    # ----------------------------------------------------------------

    tk.Label(frame1, text="Table to be deleted").grid(row=3)
    Dinsert = tk.Entry(frame1)
    Dinsert.grid(row=3, column=1)

    def doDInsert():
        db.deleteTableData(Dinsert.get())

    button = tk.Button(m, text="Delete", command=doDInsert)
    button.grid(row=3, column=2)

    # ----------------------------------------------------------------

    tk.Label(frame1, text="Table to get Averge from").grid(row=4)
    Ainsert = tk.Entry(frame1)
    Ainsert.grid(row=4, column=1)
    Acol = tk.Entry(frame1)
    tk.Label(frame1, text="Column of the table to get Averge from").grid(
        row=4, column=2)
    Acol.grid(row=4, column=3)

    def doAInsert():
        average = db.average(Ainsert.get(), Acol.get())
        tk.Label(m, text=average).grid(row=4, column=5)

    button = tk.Button(frame1, text="Submit", command=doAInsert)
    button.grid(row=4, column=4)

    # ----------------------------------------------------------------

    tk.Label(frame1, text="Show Table").grid(row=5)
    Stable = tk.Entry(frame1)
    Stable.grid(row=5, column=1)

    def doSInsert():

        select = toString(db.selectDisplay(Stable.get()))
        print(select)
        m2 = tk.Tk()

        frame3 = tk.Frame(m2)
        text = ScrolledText(frame3)

        text.insert(tk.END, select)
        frame3.grid(row=1)
        text.grid()

    button = tk.Button(frame1, text="Submit", command=doSInsert)
    button.grid(row=5, column=2)


frame = tk.Frame(m)
frame.grid(row=1)
host = tk.Entry(frame)
user = tk.Entry(frame)
pswd = tk.Entry(frame, show="*")
database = tk.Entry(frame)

tk.Label(frame, text="Host").grid(row=1)
tk.Label(frame, text="User").grid(row=2)
tk.Label(frame, text="Password").grid(row=3)
tk.Label(frame, text="Schema").grid(row=4)

host.grid(row=1, column=2)
user.grid(row=2, column=2)
pswd.grid(row=3, column=2)
database.grid(row=4, column=2)


def Login():
    db.GetUserInfo(host.get(), user.get(), pswd.get(), database.get())
    frame.grid_forget()
    app()


button = tk.Button(frame, text="Login", command=Login)
button.grid(row=5)


m.mainloop()
