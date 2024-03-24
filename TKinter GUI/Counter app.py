import tkinter as tk

class counterApp:
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        mainwindow.title("Counter App")
        mainwindow.geometry("500x300")
        mainwindow.minsize(400,180)
        mainwindow.maxsize(900,500)

        self.var = tk.IntVar(value=0)
        # add widgets
        self.lbl1 = tk.Label(mainwindow, textvariable=self.var, font=('BOLD',30))
        self.lbl1.pack()

        self.btn1 = tk.Button(mainwindow, text='Increment', command=self.increment)
        self.btn

root = tk.Tk()
root.title("Counter App")
root.geometry('500x300')
root.minsize(400,180)
root.maxsize(900,500)

var = tk.IntVar(value=0)
lbl1 = tk.Label(root, text="1")

def increment():
    data = var.get()+1
    var.set(data)
    if data >= 10:
        lbl1.config(fg="red")
    else:
        lbl1.config(fg="green")

def decrement():
    data = var.get()-1
    if data < 0:
        pass
    else:
        var.set(data)
    if data >= 10:
        lbl1.config(fg="red")
    else:
        lbl1.config(fg="green")
