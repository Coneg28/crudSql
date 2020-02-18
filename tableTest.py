import tkinter as tk
from tkinter import ttk

def viewTable():
    global tree
    tree = ttk.Treeview(root, column = (1,2,3,4,5,6), selectmode = "extended",height = "30", show = "headings") 
    tree.heading(1, text = "ID")
    tree.column(1, minwidth = 0, width = 40, anchor = 'center')
    tree.heading(2, text = "Name")
    tree.column(2, minwidth = 0, width = 120, anchor = 'center')
    tree.heading(3, text = "Price")
    tree.column(3, minwidth = 0, width = 100, anchor = 'center')
    tree.heading(4, text = "Size")
    tree.column(4, minwidth = 0, width = 80, anchor = 'center')
    tree.heading(5, text = "Description")
    tree.column(5, minwidth = 0, width = 150, anchor = 'center')
    tree.heading(1, text = "Timestamp")
    tree.column(1, minwidth = 0, width = 150, anchor = 'center')
    tree.pack(fill = 'x')

root = tk.Tk()
root.title("Table")
root.resizable(0,0)
root.geometry('600x500')
viewTable()
root.mainloop()