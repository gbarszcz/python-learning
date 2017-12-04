# coding=utf-8
# Korzystając z modułu Tkinter napisz prosty kalkulator pozwalający dodawać, odejmować, mnożyć i dzielić.
import Tkinter as tk
import tkFont

root = tk.Tk()

default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=15)
root.option_add("*Font", default_font)

number = ''
element = tk.IntVar()
total = tk.IntVar()
actions = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y,
}
action = None


def add_figure(num):
    global number, command
    number = number + num
    element.set(int(number))


def change_action(act):
    global action, number
    total.set(element.get())
    action = actions.get(act)
    number = ''


def equals(act):
    global number
    if act is not None:
        element.set(int(act(total.get(), int(number))))
        number = str(element.get())


def clear():
    global number, action
    number = ''
    element.set(0)
    total.set(0)
    action = None


# main messagebox
result = tk.Label(root, textvariable=element)
result.grid(row=0, columnspan=5)

figure = tk.StringVar()
tk.Button(root, text='7', command=lambda: add_figure('7')).grid(row=1, column=0)
tk.Button(root, text='8', command=lambda: add_figure('8')).grid(row=1, column=1)
tk.Button(root, text='9', command=lambda: add_figure('9')).grid(row=1, column=2)
tk.Button(root, text='/', command=lambda: change_action('divide')).grid(row=1, column=3)

tk.Button(root, text='C', command=clear).grid(row=1, column=4)
tk.Button(root, text='=', command=lambda: equals(action)).grid(row=2, rowspan=3, column=4, sticky=tk.N + tk.S)

tk.Button(root, text='4', command=lambda: add_figure('4')).grid(row=2, column=0)
tk.Button(root, text='5', command=lambda: add_figure('5')).grid(row=2, column=1)
tk.Button(root, text='6', command=lambda: add_figure('6')).grid(row=2, column=2)
tk.Button(root, text='*', command=lambda: change_action('multiply')).grid(row=2, column=3)

tk.Button(root, text='1', command=lambda: add_figure('1')).grid(row=3, column=0)
tk.Button(root, text='2', command=lambda: add_figure('2')).grid(row=3, column=1)
tk.Button(root, text='3', command=lambda: add_figure('3')).grid(row=3, column=2)
tk.Button(root, text='-', command=lambda: change_action('subtract')).grid(row=3, column=3)

tk.Button(root, text='0', command=lambda: add_figure('0')).grid(row=4, column=0, columnspan=3,
                                                                sticky=tk.W + tk.E)
tk.Button(root, text='+', command=lambda: change_action('add')).grid(row=4, column=3)

root.mainloop()
