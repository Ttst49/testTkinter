from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(width=50, text="Goodbye!",command=root.destroy).grid(column=0, row=5)
root.mainloop()