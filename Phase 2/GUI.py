import tkinter as tk
#import DatabaseConnector.py
import HelloWorld as hw


m = tk.Tk()

button = tk.Button(m, text="Hello World", width=25, command=hw.Hello)
button.pack()

m.mainloop()


# import tkinter as tk
# r = tk.Tk()
# r.title('Counting Seconds')
# button = tk.Button(r, text='Stop', width=25, command=r.destroy)
# button.pack()
# r.mainloop()
