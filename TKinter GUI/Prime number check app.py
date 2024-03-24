import tkinter as tk

class app:
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        mainwindow.title("Prime Number Check")
        mainwindow.geometry("500x300")
        mainwindow.minsize(400,180)
        mainwindow.maxsize(900,500)

        tk.Label(mainwindow, text = "Enter the number : ").pack()
        
        self.name = tk.Entry(mainwindow)
        self.name.pack()
        
        tk.Button(mainwindow, text = "Prime Check", command = self.action).pack()

        self.out = tk.Label(mainwindow, text = "")
        self.out.pack()

    def action(self):
        data = self.name.get()
        
        if int(data)==1:
            self.out.config(text = data + " is not a Prime number")
        if int(data)<1:
            self.out.config(text = "INVALID INPUT !!")
        else:
            count = 0
            for i in range(1,int(data)+1):
                if int(data)%i == 0:
                    count += 1
                if count == 2:
                    self.out.config(text = data+" is a Prime number !")
                else:
                    self.out.config(text = data+" is not a Prime number !")
                
        self.name.delete(0, tk.END)


# main loop

root = tk.Tk()
exe = app(root)
root.mainloop()

