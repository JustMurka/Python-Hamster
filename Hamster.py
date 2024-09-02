from tkinter import *
from tkinter import ttk
import tkinter

coin = 0

root = Tk()
root.geometry("400x600")
root.resizable(False, False)
root.title("Python Combat")

def Buttonclick():
    global coin
    coin += 1
    TextNum.config(text=coin)

Text = ttk.Label(text="Python Combat")
Text.pack()
TextNum = ttk.Label(text=coin)
TextNum.pack()
Buttoncoin = ttk.Button(text="Click", command=Buttonclick)
Buttoncoin.pack(expand=True)

root.mainloop()
