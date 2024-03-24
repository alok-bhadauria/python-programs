'''
Layout arrangement is the process of arranging widgets on a Tkinter window in Python.
There are three layout managers in Tkinter: pack, place, and grid. 
The pack() method is used to arrange widgets in a horizontal or vertical stack.
The place() method allows you to specify the exact x and y coordinates for widget placement.
The grid() method arranges widgets in a grid, similar to rows and columns.
'''

# TO DO LIST

import tkinter as tk

root = tk.Tk()
root.title('To Do List')
root.geometry('400x300')

def additem():
    data=entry.get()
    list_box.insert(tk.END, data)
    entry.delete(0, tk.END)

def deleteitem():
    select_index = list_box.curselection()
    list_box.delete(select_index)

def deleteitemall():
    list_box.delete(0, tk.END)

entry = tk.Entry(root)
entry.grid(row=0, column=0)

bt_add = tk.Button(root, text='Add Item', command=additem)
bt_add.grid(row=0, column=1)

list_box = tk.Listbox(root, width=40)
list_box.grid(row=1, column=0, columnspan=2)

bt_delete = tk.Button(root, text='Delete Selected Item', command=deleteitem)
bt_delete.grid(row=2, column=0)

bt_deleteall = tk.Button(root, text='Delete All Items', command=deleteitemall)
bt_deleteall.grid(row=2, column=1)

root.mainloop()