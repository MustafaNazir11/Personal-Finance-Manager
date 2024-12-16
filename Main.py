from tkinter import *
from register import register
from login import login

# Main Application

root = Tk()
root.title("PERSONAL FINANCE MANAGER")

    # Main Header
Label(root, text="PERSONAL FINANCE TRACKER", font=("Times New Roman", 28, "bold"), fg="blue").pack(pady=20)

    # Buttons for navigation
Button(root, text="Register", command=lambda: register(root), fg="white", bg="green", font=("Times New Roman", 12)).pack(pady=10)
Button(root, text="Login", command=lambda: login(root), fg="white", bg="green", font=("Times New Roman", 12)).pack(pady=10)


root.mainloop()
