from tkinter import *
import tkinter.font as font
import random as rd
import time
from functools import partial

win = Tk()
win.resizable(width=False, height=False)
win.title = "Match Maker"

first = True
previousX = 0
previousY = 0

colors = ["#800000", "#9A7434", "#000075", "#808000", "#911eb4", "#3cb44b",
          "#4363d8", "#f58231", "#42d4f4", "#ffe119", "#fabed4", "#ffffff",
          "#800000", "#9A7434", "#000075", "#808000", "#911eb4", "#3cb44b",
          "#4363d8", "#f58231", "#42d4f4", "#ffe119", "#fabed4", "#ffffff"]

rd.shuffle(colors)

colors_symbol = []
for i in range(len(colors)):
    if i % 6 == 0:
        colors_symbol.append([])
    colors_symbol[i // 6].append(colors[i])

buttons = {}


def showSymbol(i, j):
    global first, previousX, previousY
    buttons[i, j].configure(bg=colors_symbol[i][j])
    buttons[i, j].update_idletasks()


for i in range(4):
    for j in range(6):
        args = partial(showSymbol, i, j)
        button = Button(command=args, width=12, height=8, bg="black")
        buttons[i, j] = button
        button.grid(row=i, column=j)

win.mainloop()
