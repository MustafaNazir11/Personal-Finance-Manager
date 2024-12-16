from tkinter import *
from utility import check_user
from transaction_page import transaction_page
from income_page import go_to_income_page


def login(root):
    """Sets up the login page."""
    def handle_login():
        """Handles login logic."""
        user_email = entry_email.get()
        user_password = entry_password.get()

        username = check_user(user_email, user_password)
        if username:
            label_output.config(text=f"Welcome back, {username}!", fg="green")

            # Display buttons to choose between Transaction Page or Income Page
            for widget in root.winfo_children():
                widget.destroy()

            Label(root, text=f"Welcome, {username}!", font=("Times New Roman", 18, "bold"), fg="blue").pack(pady=20)
            Label(root, text="Choose an action:", font=("Times New Roman", 14)).pack(pady=10)

            Button(root, text="Transaction Page", command=lambda: transaction_page(root, username), fg="white", bg="blue", font=("Times New Roman", 12)).pack(pady=20)
            Button(root, text="Income Page", command=lambda: go_to_income_page(root), fg="white", bg="green", font=("Times New Roman", 12)).pack(pady=20)
        else:
            label_output.config(text="Invalid email or password.", fg="red")

    # Clear the root window
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Login", font=("Times New Roman", 18, "bold")).pack(pady=10)

    Label(root, text="Email:").pack()
    entry_email = Entry(root, width=50, font=("Times New Roman", 18))
    entry_email.pack()

    Label(root, text="Password:").pack()
    entry_password = Entry(root, width=50, show="*", font=("Times New Roman", 18))
    entry_password.pack()

    Button(root, text="Login", command=handle_login, fg="white", bg="green", font=("Times New Roman", 12)).pack(pady=20)
    global label_output
    label_output = Label(root, text="", fg="red", font=("Times New Roman", 18))
    label_output.pack()
