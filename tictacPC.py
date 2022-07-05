from tkinter import *
import os
from random import randint

window =Tk()
menu = Menu(window)
window.config(menu=menu)
submenu = Menu(menu, tearoff = 0)
window.geometry("320x430")

board = [['','',''],['','',''],['','','']]
count = 0

def winning_combos():
    if (board[0][0] == board[0][1] == board[0][2] == 'x' or board[1][0] == board[1][1] == board[1][2] == 'x' or board[2][0] == board[2][1] == board[2][2] == 'x' or
    board[0][0] == board[1][0] == board[2][0] == 'x' or board[0][1] == board[1][1] == board[2][1] =='x' or board[0][2] == board[1][1] == board[2][2] =='x' or
    board[0][0] == board[1][1] == board[2][2] == 'x' or board[0][2] == board[1][1] == board[2][0] == 'x'):
        turn['text'] = 'Player X wins'
        turn['fg'] = 'red'
    elif (board[0][0] == board[0][1] == board[0][2] == 'o' or board[1][0] == board[1][1] == board[1][2] == 'o' or board[2][0] == board[2][1] == board[2][2] == 'o' or
    board[0][0] == board[1][0] == board[2][0] == 'o' or board[0][1] == board[1][1] == board[2][1] =='o' or board[0][2] == board[1][1] == board[2][2] =='o' or
    board[0][0] == board[1][1] == board[2][2] == 'o' or board[0][2] == board[1][1] == board[2][0] == 'o'):
        turn['text'] = 'Player O wins'
        turn['fg'] = 'blue'
    elif count == 9:
        turn['text'] = 'Its a tie'

def button_changer(button, x, y):
    global count
    global board 
    if  button['text'] == '':
        if count % 2 == 0:
            button['text'] = 'X'
            button['fg'] = 'red'
            board[x][y] = 'x'
        else:
            button['text'] = 'O'
            button['fg'] = 'blue'
            board[x][y] = 'o'
        count += 1
        label_changer()
        winning_combos()

def label_changer():
    global count
    if count % 2 == 0:
        turn['text'] = 'Player X turn'
    else:
        turn['text'] = 'Player O turn'

def clear_the_board():
    pass

def pc_move():
    pass
    
menu.add_cascade(labe="Menu", menu=submenu)
submenu.add_command(label="Play again", command=clear_the_board())
submenu.add_command(label="Exit", command=window.destroy)
         
button1 = Button(window, text="", fg='black', height= 5, width=10, command=lambda: button_changer(button1, 0, 0))
button2 = Button(window, text="", fg='black', height= 5, width=10, command=lambda: button_changer(button2, 0, 1))
button3 = Button(window, text="", fg='black', height= 5, width=10, command=lambda: button_changer(button3, 0, 2))
button4 = Button(window, text="", fg='black', height= 5, width=10, command=lambda: button_changer(button4, 1, 0))
button5 = Button(window, text="", fg='black', height= 5, width=10, command=lambda: button_changer(button5, 1, 1))
button6 = Button(window, text="", fg='black', height= 5, width=10, command=lambda: button_changer(button6, 1, 2))
button7 = Button(window, text="", fg='black', height= 5, width=10, command=lambda: button_changer(button7, 2, 0))
button8 = Button(window, text="", fg='black', height= 5, width=10, command=lambda: button_changer(button8, 2, 1))
button9 = Button(window, text="", fg='black', height= 5, width=10, command=lambda: button_changer(button9, 2, 2))

turn = Label(window, text="Player X turn", fg='black')

button1.grid(row=1, column=0, sticky=W)
button2.grid(row=1, column=1, sticky=W)
button3.grid(row=1, column=2, sticky=W)
button4.grid(row=2, column=0, sticky=W)
button5.grid(row=2, column=1, sticky=W)
button6.grid(row=2, column=2, sticky=W)
button7.grid(row=3, column=0, sticky=W)
button8.grid(row=3, column=1, sticky=W)
button9.grid(row=3, column=2, sticky=W)
turn.grid(row=4, column =1, columnspan=3, sticky=W)

window.mainloop()