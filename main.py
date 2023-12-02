from tkinter import *


global zoneCalcul

root = Tk()
root.title("Calcule Tout")
root.geometry("800x620")
root.resizable(False,False)

expression = ""

input_text = StringVar()


def button_click(nbr):
    global expression
    expression += str(nbr)
    input_text.set(expression)


def button_clear():
    global expression
    expression = ""
    input_text.set(expression)


def calculate_button():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

input_frame = Frame(root,
                    width=312,
                    height=50,
                    bd=0,
                    highlightbackground="black",
                    highlightcolor="black",
                    highlightthickness=2)

input_frame.pack(side=TOP)

input_field = Entry(input_frame,
                    font=('helvetica', 18, 'bold'),
                    textvariable=input_text,
                    width=50,
                    bg="#eee",
                    bd=0,
                    justify=RIGHT)

input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = Frame(root, width=312, height=272.5, bg="grey")

btns_frame.pack()


clear = Button(btns_frame,
               text="C",
               fg="black",
               width=32,
               height=3,
               bd=0,
               bg="#eee",
               cursor="hand2",
               command=lambda: button_clear()).grid(row=0, column=0, columnspan = 3, padx = 1, pady = 1)

divide = Button(btns_frame,
                text = "/",
                fg = "black",
                width = 10,
                height = 3,
                bd = 0,
                bg = "#eee",
                cursor = "hand2",
                command = lambda: button_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)


seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(7)).grid(row=1, column=0, padx=1, pady=1)

eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(8)).grid(row=1, column=1, padx=1, pady=1)

nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: button_click(9)).grid(row=1, column=2, padx=1, pady=1)

multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: button_click("*")).grid(row=1, column=3, padx=1, pady=1)

# third row

four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: button_click(4)).grid(row=2, column=0, padx=1, pady=1)

five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: button_click(5)).grid(row=2, column=1, padx=1, pady=1)

six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: button_click(6)).grid(row=2, column=2, padx=1, pady=1)

minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: button_click("-")).grid(row=2, column=3, padx=1, pady=1)

# fourth row

one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: button_click(1)).grid(row=3, column=0, padx=1, pady=1)

two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: button_click(2)).grid(row=3, column=1, padx=1, pady=1)

three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(3)).grid(row=3, column=2, padx=1, pady=1)

plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
              command=lambda: button_click("+")).grid(row=3, column=3, padx=1, pady=1)

# fourth row

zero = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: button_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: button_click(".")).grid(row=4, column=2, padx=1, pady=1)

equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: calculate_button()).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()