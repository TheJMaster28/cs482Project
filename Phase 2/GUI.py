import tkinter as tk
import DatabaseConnector as db
import HelloWorld as hw
m = tk.Tk()


def app():
    global m
    tk.Label(m, text="Path to File for Single Insert").grid(row=0)
    insert = tk.Entry(m)
    insert.grid(row=0, column=1)

    def doInsert():
        db.singlePlayersInsert(insert.get())

    button = tk.Button(m, text="Submit", command=doInsert)
    button.grid(row=0, column=2)

    # ---------------------------------------------------------------

    tk.Label(m, text="Path to File for Multi Insert").grid(row=1)
    Minsert = tk.Entry(m)
    Minsert.grid(row=1, column=1)
    Mtable = tk.Entry(m)
    tk.Label(m, text="Table to insert to").grid(row=1, column=2)
    Mtable.grid(row=1, column=3)

    def doMInsert():
        db.multInsert(Minsert.get(), Mtable.get())

    button = tk.Button(m, text="Submit", command=doMInsert)
    button.grid(row=1, column=4)


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
