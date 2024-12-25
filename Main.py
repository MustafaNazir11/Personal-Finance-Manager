from tkinter import *
from register import register
from login import login
from about_page import about_page

root = Tk()
root.title("Personal Finance Manager")
root.geometry("400x400")
root.configure(bg="#d3d3d3")

Label(
    root,
    text="PERSONAL FINANCE TRACKER",
    font=("Helvetica", 22, "bold"),
    fg="#000080",
    bg="#d3d3d3"
).pack(pady=30)

Button(
    root,
    text="Register",
    command=lambda: register(root),
    fg="white",
    bg="#004080",
    font=("Helvetica", 14, "bold"),
    width=15,
    height=2,
    relief="raised",
    bd=4
).pack(pady=15)

Button(
    root,
    text="Login",
    command=lambda: login(root),
    fg="white",
    bg="#004080",
    font=("Helvetica", 14, "bold"),
    width=15,
    height=2,
    relief="raised",
    bd=4
).pack(pady=15)

Button(
    root,
    text="About",
    command=lambda: about_page(root),
    fg="white",
    bg="#2c2c2c",
    font=("Helvetica", 14, "bold"),
    width=15,
    height=2,
    relief="raised",
    bd=4
).pack(pady=15)

root.mainloop()
