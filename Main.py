from tkinter import *
from register import register
from login import login
from about_page import about_page

def main_page(root):
    """
    Sets up the homepage with navigation options.
    """
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Personal Finance Manager")
    root.configure(bg="#d3d3d3")

    Label(
        root,
        text="PERSONAL FINANCE MANAGER",
        font=("Helvetica", 22, "bold", "underline"),
        fg="#000080",
        bg="#d3d3d3"
    ).pack(pady=30)

    Button(
        root,
        text="Register",
        command=lambda: register(root, main_page),
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
        command=lambda: login(root, main_page),
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
        command=lambda: about_page(root, main_page),
        fg="white",
        bg="#2c2c2c",
        font=("Helvetica", 14, "bold"),
        width=15,
        height=2,
        relief="raised",
        bd=4
    ).pack(pady=15)

if __name__ == "__main__":
    root = Tk()
    root.geometry("500x400")
    main_page(root)
    root.mainloop()
