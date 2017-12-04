# coding=utf-8
# Napisz prosty sekundnik odliczający czas do zadanego momentu. Odliczanie rozpoczyna się po wciśnięciu przycisku "start".
# Kiedy czas się skończy odliczanie zatrzymuje się, a program wyświetla komunikat o zakończeniu odliczania.

import Tkinter as tk

root = tk.Tk()


def start():
    global now
    now.set(entry.get())
    update_label()
    global label
    label.configure(text="")


def update_label():
    global now
    now.set(now.get() - 1)
    if now.get() > 0:
        root.after(1000, update_label)
    else:
        global label
        label.configure(text="Timer has stopped.")


tk.Label(root, text="Set timer: ").grid(row=0, column=0)

entry = tk.Entry(root)
entry.grid(row=0, column=1)

tk.Button(root, text="start", command=start).grid(row=1, column=0)

now = tk.IntVar()
tk.Label(root, textvariable=now).grid(row=2, column=0)
label = tk.Label(root)
label.grid(row=3, column=0)
root.mainloop()
