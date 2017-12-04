# coding=utf-8
# Przygotuj okno skłądające się z jednego buttonu i trzech radioButtonów określających podstawowe kolory.
# Zmiana zaznaczenia radio zmienia kolor tekstu na przycisku.
# Wciśnięcie przycisku powoduje wyświetlenie dowolnego komunikatu.

import Tkinter as tk

root = tk.Tk()


def button_click():
    print "Button color: " + varRadio1.get()


def change_color():
    button.config(fg=varRadio1.get())


varRadio1 = tk.StringVar()
tk.Radiobutton(root, text="red", value="red", variable=varRadio1, command=change_color).pack()
tk.Radiobutton(root, text="green", value="green", variable=varRadio1, command=change_color).pack()
tk.Radiobutton(root, text="blue", value="blue", variable=varRadio1, command=change_color).pack()

button = tk.Button(root, text="Button", command=button_click)
button.pack()
root.mainloop()
