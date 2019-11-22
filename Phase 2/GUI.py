import tkinter as tk
import DatabaseConnector as db
import HelloWorld as hw
m = tk.Tk()


def app():
    global m

    tk.Label(m, text="Path to File for insert").grid(row=0)
    insert = tk.Entry(m)
    insert.grid(row=0, column=1)

    def doInsert():
        db.singlePlayersInsert(insert.get())

    button = tk.Button(m, text="Submit", command=doInsert)
    button.grid(row=0, column=2)


if (db.user == ""):
    print("here")
    db.GetUserInfo()
    app()


m.mainloop()
