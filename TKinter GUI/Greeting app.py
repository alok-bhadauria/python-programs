import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Greetings App")
root.geometry('500x300')
root.minsize(400,180)
root.maxsize(900,500)

def display_message():
    user_input = entry.get()
    message = "Hello, " + user_input + "!"
    messagebox.showinfo("Greetings", message)

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=display_message)
button.pack()

root.mainloop()