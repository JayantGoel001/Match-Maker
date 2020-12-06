from tkinter import *
import random as rd
import time

win = Tk()
win.resizable(width=False, height=False)
win.title = "Match Maker"

first = True
previousX = 0
previousY = 0

button_symbol = [["\u2702", "\u2705", "\u2708", "\u2709", "\u270A", "\u270B"],
                 ["\u270C", "\u270F", "\u2712", "\u2714", "\u2716", "\u2728"],
                 ["\u2702", "\u2705", "\u2708", "\u2709", "\u270A", "\u270B"],
                 ["\u270C", "\u270F", "\u2712", "\u2714", "\u2716", "\u2728"]]

rd.shuffle(button_symbol)
for i in button_symbol:
    rd.shuffle(i)

buttons = {}
for i in range(4):
    for j in range(6):
        button = Button(width=12, height=8)
        button.grid(row=i, column=j)
        buttons[i, j] = button



win.mainloop()
