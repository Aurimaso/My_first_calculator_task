
from tkinter import StringVar, Tk, Menu, Button, W, Label
from app import calc_eval, sqrt_func
import logging

logging.basicConfig(filename='calculations.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

window =Tk()
window.title('Calculator')
user_input = StringVar()
menu = Menu(window)
window.config(menu=menu)
submenu = Menu(menu, tearoff = 0)
window.geometry("320x430")
menu.add_cascade(label="Menu", menu=submenu)
submenu.add_command(label="Exit", command=window.destroy)

starting_text = ""
input_text = StringVar()

def printing(num:int) -> None:
    global starting_text
    starting_text = starting_text + str(num)
    input_text.set(starting_text)

def clearing() -> None:
    global starting_text
    starting_text = ""
    input_text.set(starting_text)

def equal() -> None:
    global starting_text
    starting_text = calc_eval(starting_text)
    input_text.set(starting_text)

def sqrt_button() -> None:
    global starting_text
    starting_text = sqrt_func(starting_text)
    input_text.set(starting_text)
    

button_eql = Button(window, text="=",height= 5, width=10, bg='#DFDFDF', command=lambda: equal())
button1 = Button(window, text="1",height= 5, width=10, command=lambda: printing(1))
button2 = Button(window, text="2",height= 5, width=10, command=lambda: printing(2))
button3 = Button(window, text="3",height= 5, width=10, command=lambda: printing(3))
button4 = Button(window, text="4",height= 5, width=10, command=lambda: printing(4))
button5 = Button(window, text="5",height= 5, width=10, command=lambda: printing(5))
button6 = Button(window, text="6",height= 5, width=10, command=lambda: printing(6))
button7 = Button(window, text="7",height= 5, width=10, command=lambda: printing(7))
button8 = Button(window, text="8",height= 5, width=10, command=lambda: printing(8))
button9 = Button(window, text="9",height= 5, width=10, command=lambda: printing(9))
button0 = Button(window, text="0",height= 5, width=10, command=lambda: printing(0))
button_dot = Button(window, text=".",height= 5, width=10, command=lambda: printing('.'))
button_C = Button(window, text="C",height= 5, width=10, bg='#FCB6B6', command=lambda: clearing())
button_dev = Button(window, text="/",height= 5, width=10, command=lambda: printing('/'))
button_multi = Button(window, text="X",height= 5, width=10, command=lambda: printing('*'))
button_min = Button(window, text="-",height= 5, width=10, command=lambda: printing('-'))
button_plus = Button(window, text="+",height= 5, width=10, command=lambda: printing('+'))
button_sqrt = Button(window, text="√",height= 5, width=10, command=lambda: sqrt_button())
window.bind("<Return>", lambda event: equal())

entry_field = Label(window, textvariable=input_text, width=17, font=('Helvetica 12'))

entry_field.grid(row=0, column=0, columnspan=2)
button_C.grid(row=0, column=2)
button_dev.grid(row=0, column=3)

button1.grid(row=1, column=0, sticky=W)
button2.grid(row=1, column=1, sticky=W)
button3.grid(row=1, column=2, sticky=W)
button_multi.grid(row=1, column=3, sticky=W)
button4.grid(row=2, column=0, sticky=W)
button5.grid(row=2, column=1, sticky=W)
button6.grid(row=2, column=2, sticky=W)
button_min.grid(row=2, column=3, sticky=W)
button7.grid(row=3, column=0, sticky=W)
button8.grid(row=3, column=1, sticky=W)
button9.grid(row=3, column=2, sticky=W)
button_plus.grid(row=3, column=3, sticky=W)
button_dot.grid(row=4, column=0, sticky =W)
button0.grid(row=4, column=1, sticky=W)
button_eql.grid(row=4, column=3, sticky=W)
button_sqrt.grid(row=4, column=2, sticky=W)

window.mainloop()