#creat a login in python
import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "123456":
        messagebox.showinfo("Login Successful", "Welcome, admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

root = tk.Tk()