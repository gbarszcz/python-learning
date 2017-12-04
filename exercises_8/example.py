# TKinter

import Tkinter as tk
import tkFont


# funkcja ktora zmienia wyglad labela
def labelConfig(label, txt):
    label.config(text=txt, fg="light green", bg="dark green")


root = tk.Tk()
# l = tk.Label(root, text="Hello Tkinter!")
# l.pack() # dopasowanie okna
# labelConfig(l, "123")

# globalna modyfikacja czcionki
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=9)
root.option_add("*Font", default_font)


# wyswietlanie na siatce
# scalanie kolumn - columnspan. wyrownanie: sticky=tk.W
# label1 = tk.Label(root, text="label1", bg="green")
# label1.grid(row=0, column=0, columnspan=2)
# label2 = tk.Label(root, text="label2", bg="blue")
# label2.grid(row=0, column=1)
# label3 = tk.Label(root, text="label3", bg="yellow")
# label3.grid(row=1, column=0)
# label4 = tk.Label(root, text="label4", bg="red")
# label4.grid(row=1, column=1)
# label5 = tk.Label(root, text="label5", bg="red")
# label5.grid(row=1, column=2)
# label6 = tk.Label(root, text="label6", bg="red")
# label6.grid(row=2, column=1, columnspan=2)

# obsluga przycisku
# def button_click():
#     print "click"
#
#
# def get_button_text():
#     print s1.get()
#
#
# x = 0
#
#
# def add(ent, y):
#     global x
#     x += y
#     ent.delete(0, 'end')
#     ent.insert(tk.END, str(x))


# message box
# tk.Label(root, text="Write something").grid(row=0)
# s1 = tk.Entry(root)
# s1.grid(row=0, column=0, columnspan=2)
# tk.Button(root, text="OK", command=get_button_text).grid(row=1, column=0)
# tk.Button(root, text="1", command=lambda: add(s1, 1)).grid(row=1, column=1)
# tk.Button(root, text="2", command=lambda: add(s1, 2)).grid(row=1, column=2)

# def show_var1():
#     print var1.get()
#
# def show_var2():
#     print var2.get()

# checkbox
# var1 = tk.BooleanVar()
# var2 = tk.BooleanVar()
# tk.Checkbutton(root, text="Check 1", variable=var1).grid(row=0, column=0)
# tk.Checkbutton(root, text="Check 2", variable=var2).grid(row=0, column=1)
# tk.Button(root, text="print 1", command=show_var1).grid(row=0, column=2)
# tk.Button(root, text="print 2", command=show_var2).grid(row=0, column=3)

# def show_radio():
#     print varRadio1.get()
# # radio
# varRadio1 = tk.IntVar()
# tk.Radiobutton(root, text="option 1", value=1, variable=varRadio1).pack()
# tk.Radiobutton(root, text="option 2", value=2, variable=varRadio1).pack()
#
# varRadio2 = tk.IntVar()
# tk.Radiobutton(root, text="option 1", value=1, variable=varRadio2).pack()
# tk.Radiobutton(root, text="option 2", value=2, variable=varRadio2).pack()

# textarea
# textArea = tk.Text(root, height=10, width=50)
# textArea.pack(side=tk.LEFT, fill=tk.Y)
# slider = tk.Scrollbar(root)
# slider.pack(side=tk.RIGHT, fill=tk.Y)
# slider.configure(command=textArea.yview)
# textArea.config(yscrollcommand=slider.set)
# textArea.insert(tk.END, "sample")

# canvas

w = tk.Canvas(root, width=200, height=100)
w.pack()
w.create_rectangle(50,20,150,80,fill="red")
w.create_line(0,0,50,20,fill="blue",width=3)
w.create_line(0,100,50,80,fill="yellow3",width=4)

root.mainloop()


# praca domowa: zadanie 1 (na 2 pkt, nieobowiazkowe)
