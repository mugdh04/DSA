import tkinter as tk
from tkinter import messagebox

def check():
    y = x.get()
    t = float(y)
    if (t%2 == 0):
        Even = str(t) + " is an EVEN Number."
        messagebox.showinfo("Even Check",Even)
    elif (t%2 != 0):
        Odd = str(t) + " is an ODD Number."
        messagebox.showinfo("Odd Check",Odd)
    else:
        Error = "The Number entered was incorrect."
        messagebox.showinfo("Error",Error)

root = tk.Tk()
root.geometry('400x100')
var1 = tk.Label(root, text = "Enter any no. to check the")
var1.grid(row = 0, column = 0)
var2 = tk.Label(root, text = "number is odd or even: ")
var2.grid(row = 0, column = 1)
x = tk.Entry(root)
x.grid(row = 0, column = 2)
var3 = tk.Label(root,text = " ")
var3.grid(row = 1, column = 1)
var4 = tk.Label(root,text = " ")
var4.grid(row = 2, column = 1)
B = tk.Button(root, text = "Check", command = check)
B.grid(row = 3, column = 1)
tk.mainloop()