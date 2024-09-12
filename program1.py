import tkinter as tk
from tkinter import *
from tkinter import END
from tkinter import Button
from tkinter import Entry

root = tk.Tk()
root.title("Simple Calculator")

user_input = Entry(root, width=30, font=('Arial', 15), borderwidth=4)
user_input.grid(row=0, column=0, columnspan=4,padx=10,pady=10,ipady=10)

def add_to_input(number):
    current = user_input.get()
    user_input.delete(0,END)
    user_input.insert(0, current + str(number))

def clear_input():
    user_input.delete(0, END)

def math():
    try:
        calculation = user_input.get()
        result = eval(calculation)
        user_input.delete(0, END)
        user_input.insert(0, result)
    except:
        user_input.delete(0,END)
        user_input.insert(0 , "Division Invalid")

button_style = {
    'font' : ('Arial', 13),
    'bg' : 'grey',
    'fg' : 'black',
    'padx' : 30,
    'pady' : 20,
    'borderwidth' : 2,
}

buttons = [("7","8","9","/"),("4","5","6","*"),("1","2","3","-"),("0","Clear","=","+")]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == "Clear":
            button = Button(root, text=text, command=clear_input, **button_style)
        elif text =="=":
            button = Button(root, text=text, command= math,padx = 88,pady=20,font = ('Arial',15))
        else:
            button = Button(root, text=text, command=lambda t=text: add_to_input(t), **button_style)
        button.grid(row=i+1, column = j,padx=4,pady=4)

root.mainloop()
