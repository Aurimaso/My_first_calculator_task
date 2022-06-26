
from tkinter import *


window =Tk()
user_input = StringVar()
menu = Menu(window)
window.config(menu=menu)
submenu = Menu(menu, tearoff = 0)
window.geometry("350x450")
menu.add_cascade(labe="Menu", menu=submenu)

submenu.add_command(label="Exit", command=window.destroy)


button_eql = Button(window, text="=",height= 5, width=10)
button1 = Button(window, text="1",height= 5, width=10)
button2 = Button(window, text="2",height= 5, width=10)
button3 = Button(window, text="3",height= 5, width=10)
button4 = Button(window, text="4",height= 5, width=10)
button5 = Button(window, text="5",height= 5, width=10)
button6 = Button(window, text="6",height= 5, width=10)
button7 = Button(window, text="7",height= 5, width=10)
button8 = Button(window, text="8",height= 5, width=10)
button9 = Button(window, text="9",height= 5, width=10)
button0 = Button(window, text="0",height= 5, width=10)
button_C = Button(window, text="C",height= 5, width=10)
button_dev = Button(window, text="/",height= 5, width=10)
button_multi = Button(window, text="X",height= 5, width=10)
button_min = Button(window, text="-",height= 5, width=10)
button_plus = Button(window, text="+",height= 5, width=10)


field = Entry(window)
result = Label(window, text="")
status = Label(window, text="Calculating...", bd=1, relief=SUNKEN, anchor=W)

field.grid(row=0, column=0, columnspan=2)
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
button0.grid(row=4, column=1, sticky=W)
button_eql.grid(row=4, column=2, sticky=W)


result.grid(row=6, column=0)
# status.grid(row=7, column=0)

window.mainloop()