import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('BMI Calculator')
root.geometry('400x300')

def bmicalc():
    height = float(entry_height.get())
    weight = float(entry_weight.get())
    bmi = round(weight/(height**2),2)
    if bmi >= 30:
        messagebox.showinfo("BMI",f"YOUR BMI IS : {bmi} \nSTATUS : OBESE !")
    elif bmi >= 25:
        messagebox.showinfo("BMI",f"YOUR BMI IS : {bmi} \nSTATUS : OVERWEIGHT !")
    elif bmi >= 18.5:
        messagebox.showinfo("BMI",f"YOUR BMI IS : {bmi} \nSTATUS : HEALTHY !")
    elif bmi < 18.5:
        messagebox.showinfo("BMI",f"YOUR BMI IS : {bmi} \nSTATUS : UNDERWEIGHT !")
    else:
        messagebox.showinfo("BMI","Some error occured while calculating BMI !")

lbl1 = tk.Label(root, text="Enter height (in meters): ", font="comicsans 12 italic").pack()

entry_height = tk.Entry(root)
entry_height.pack(pady=5)

lbl2 = tk.Label(root, text="Enter weight (in kg): ", font="comicsans 12 italic").pack()

entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

bt_calc = tk.Button(root, text="Calculate BMI", font="hightowertext 16 bold", command=bmicalc, bg="BLACK", fg="WHITE", borderwidth=5, relief="solid").pack(pady=15)

root.mainloop()