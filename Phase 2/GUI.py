import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
import DatabaseConnector as db
#import HelloWorld as hw

m = tk.Tk()

# toString
# creates string from lists that is return from select * SQL query
def toString(string):
    s = ""
    for i in string:
        for k in i:
            s += str(k)
            s += ", "
        s += "\n"
    return s
# end of toString


# app
# main page of app
def app():
    global m

    def fileSearch(Entry):
        tk.filename = filedialog.askopenfilename(
            initialdir="/", title="Select file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        Entry.delete(0, tk.END)
        Entry.insert(10, tk.filename)

    frame1 = tk.Frame(m).grid()
    tk.Label(frame1, text="Path to File for Single Insert Players Table").grid(row=0)
    Player_insert = tk.Entry(frame1)
    Player_insert.grid(row=0, column=1)

    def doPlayersInsert():
        db.singlePlayersInsert(Player_insert.get())

    button = tk.Button(m, text="Select File",
                       command=lambda: fileSearch(Player_insert))
    button.grid(row=0, column=2)

    button = tk.Button(frame1, text="Submit", command=doPlayersInsert)
    button.grid(row=0, column=3)

    #----------------------------------------------------------------

    tk.Label(frame1, text="Path to File for Single Insert Teams Table").grid(row=1)
    Teams_insert = tk.Entry(frame1)
    Teams_insert.grid(row=1, column=1)

    def doTeamsInsert():
        db.singleTeamsInsert(Teams_insert.get())

    button = tk.Button(m, text="Select File",
                       command=lambda: fileSearch(Teams_insert))
    button.grid(row=1, column=2)

    button = tk.Button(frame1, text="Submit", command=doTeamsInsert)
    button.grid(row=1, column=3)

    # ---------------------------------------------------------------

    tk.Label(frame1, text="Path to File for Single Insert Games Table").grid(row=2)
    Games_insert = tk.Entry(frame1)
    Games_insert.grid(row=2, column=1)

    def doGamesInsert():
        db.singleGamesInsert(Games_insert.get())

    button = tk.Button(m, text="Select File",
                       command=lambda: fileSearch(Games_insert))
    button.grid(row=2, column=2)

    button = tk.Button(frame1, text="Submit", command=doGamesInsert)
    button.grid(row=2, column=3)

    # ---------------------------------------------------------------

    tk.Label(frame1, text="Path to File for Single Insert Play Table").grid(row=3)
    Play_insert = tk.Entry(frame1)
    Play_insert.grid(row=3, column=1)

    def doPlayInsert():
        db.singlePlayInsert(Play_insert.get())

    button = tk.Button(m, text="Select File",
                       command=lambda: fileSearch(Play_insert))
    button.grid(row=3, column=2)

    button = tk.Button(frame1, text="Submit", command=doPlayInsert)
    button.grid(row=3, column=3)

    # ---------------------------------------------------------------

    tk.Label(m, text="Path to File for Multi Insert").grid(row=4)
    Minsert = tk.Entry(frame1)
    Minsert.grid(row=4, column=1)
    Mtable = tk.Entry(frame1)
    tk.Label(frame1, text="Table to insert to").grid(row=4, column=3)
    Mtable.grid(row=4, column=4)

    def doMInsert():
        print(db.multInsert(Minsert.get(), Mtable.get()))

    button = tk.Button(m, text="Select File",
                       command=lambda: fileSearch(Minsert))
    button.grid(row=4, column=2)

    button = tk.Button(frame1, text="Submit", command=doMInsert)
    button.grid(row=4, column=5)

    # ----------------------------------------------------------------

    tk.Label(m, text="Path to File for Load Data Insert").grid(row=5)
    Linsert = tk.Entry(frame1)
    Linsert.grid(row=5, column=1)
    Ltable = tk.Entry(m)
    tk.Label(frame1, text="Table to insert to").grid(row=5, column=3)
    Ltable.grid(row=5, column=4)

    def doLInsert():
        db.loadData(Linsert.get(), Ltable.get())

    button = tk.Button(m, text="Select File",
                       command=lambda: fileSearch(Linsert))
    button.grid(row=5, column=2)

    button = tk.Button(frame1, text="Submit", command=doLInsert)
    button.grid(row=5, column=5)

    # ----------------------------------------------------------------

    tk.Label(frame1, text="Table to be deleted").grid(row=6)
    Dinsert = tk.Entry(frame1)
    Dinsert.grid(row=6, column=1)

    def doDInsert():
        db.deleteTableData(Dinsert.get())

    button = tk.Button(m, text="Delete", command=doDInsert)
    button.grid(row=6, column=2)

    # ----------------------------------------------------------------

    tk.Label(frame1, text="Table to get Averge from").grid(row=7)
    Ainsert = tk.Entry(frame1)
    Ainsert.grid(row=7, column=1)
    Acol = tk.Entry(frame1)
    tk.Label(frame1, text="Column of the table to get Averge from").grid(
        row=7, column=2)
    Acol.grid(row=7, column=3)

    def doAInsert():
        average = db.average(Ainsert.get(), Acol.get())
        tk.Label(m, text=average).grid(row=7, column=5)

    button = tk.Button(frame1, text="Submit", command=doAInsert)
    button.grid(row=7, column=4)

    # ----------------------------------------------------------------

    tk.Label(frame1, text="Show Table").grid(row=8)
    Stable = tk.Entry(frame1)
    Stable.grid(row=8, column=1)

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
    button.grid(row=8, column=2)
# end of app


# login page to get database information
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
    db.getUserInfo(host.get(), user.get(), pswd.get(), database.get())
    frame.grid_forget()
    app()


button = tk.Button(frame, text="Login", command=Login)
button.grid(row=5)


m.mainloop()
