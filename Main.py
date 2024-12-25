from tkinter import *
from register import register
from login import login
from about_page import about_page

# Main Application

root = Tk()
root.title("PERSONAL FINANCE MANAGER")

    # Main Header
Label(root, text="PERSONAL FINANCE TRACKER", font=("Times New Roman", 28, "bold"), fg="blue").pack(pady=20)

    # Buttons for navigation
Button(root, text="Register", command=lambda: register(root), fg="white", bg="green", font=("Times New Roman", 12)).pack(pady=10)
Button(root, text="Login", command=lambda: login(root), fg="white", bg="green", font=("Times New Roman", 12)).pack(pady=10)
Button(root, text="about", command=lambda: about_page(root), fg="black", font=("Times New Roman", 12)).pack(pady=10,side="left")

root.mainloop()
