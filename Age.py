"""
print("Enter birth year: ")
birth_year=int(input())
print("Present year: ")
present_year=int(input())
age=present_year-birth_year
print("your age is ", age)

"""
import tkinter as tk
from tkinter import messagebox
import datetime
def cal_age():
    try:
        birth_year=int(entry_birth_year.get())
        curr_year=datetime.datetime.now().year
        age=curr_year - birth_year
        messagebox.showinfo("Age Calculator", f"You are {age} years old.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid yaer.")
        
root=tk.Tk()
root.title("Age Calculator")

label_birth_year=tk.Label(root, text="Enter your birth year: ")
label_birth_year.pack(pady=10)

entry_birth_year=tk.Entry(root)
entry_birth_year.pack(pady=10)

cal_button=tk.Button(root, text="Calculate", command=cal_age)
cal_button.pack(pady=20)

root.mainloop()
