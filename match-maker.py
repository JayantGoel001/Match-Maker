import random as rd
import time
from functools import partial
from tkinter import *

win = Tk()
win.resizable(width=False, height=False)
win.title = "Match Maker"

first = True
previousX = 0
previousY = 0

colors = ["#800000", "#9A7434", "#000075", "#808000", "#911eb4", "#3cb44b",
          "#4363d8", "#f58231", "#42d4f4", "#ffe119", "#fabed4", "#000000",
          "#800000", "#9A7434", "#000075", "#808000", "#911eb4", "#3cb44b",
          "#4363d8", "#f58231", "#42d4f4", "#ffe119", "#fabed4", "#000000"]

rd.shuffle(colors)

colors_symbol = []
for i in range(len(colors)):
    if i % 6 == 0:
        colors_symbol.append([])
    colors_symbol[i // 6].append(colors[i])

buttons = {}

count = 0


def showSymbol(i, j):
    global first, previousX, previousY, count
    buttons[i, j].configure(bg=colors_symbol[i][j])
    buttons[i, j].update_idletasks()

    if first:
        previousX = i
        previousY = j
        first = False
    elif previousX != i or previousY != j:
        if colors_symbol[previousX][previousY] != colors_symbol[i][j]:
            time.sleep(0.5)
            buttons[i, j].configure(bg="white")
            buttons[previousX, previousY].configure(bg="white")
        else:
            buttons[previousX, previousY]['command'] = DISABLED
            buttons[i, j]['command'] = DISABLED
            count += 2
            if count == 24:
                win2 = Tk()
                text = Text(win2)
                text.insert(INSERT, "Congratulation!!!\nYou Won")
                text.pack()
                win2.geometry("150x50")
                win2.mainloop()
        first = True


for i in range(4):
    for j in range(6):
        args = partial(showSymbol, i, j)
        button = Button(command=args, width=12, height=8, bg="white")
        buttons[i, j] = button
        button.grid(row=i, column=j)

win.mainloop()
