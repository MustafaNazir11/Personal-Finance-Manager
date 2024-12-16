from tkinter import *
import pandas as pd
import os
from datetime import datetime
from login import login


categories = ["Food", "Rent", "Shopping", "Utilities", "Transport", "Others"]
df_transaction = pd.DataFrame(columns=categories)

def register(root):
    """Sets up the registration page."""
    

    def handle_registration():
        """Handles user registration logic."""
        global username
        user_name = entry_name.get()
        user_email = entry_email.get()
        user_password = entry_password.get()

        global username
        username = user_email.split("@")[0]
        
        new_data = pd.DataFrame({
            "timestamp": [datetime.now().strftime("%d|%m|%Y %H:%M:%S")],
            "name": [user_name],
            "email": [user_email],
            "password": [user_password]
        })

        if os.path.exists("result.csv"):
            new_data.to_csv('result.csv', mode='a', index=False, header=False)
        else:
            new_data.to_csv('result.csv', mode='w', index=False, header=True)

        # Output label with a success message
        label_output.config(
            text=f"User registered successfully! Your username is '{username}'", fg="green"
        )

        # Navigate to transaction page
        login(root)

    

    # Clear the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Registration Page UI
    Label(root, text="Register User", font=("Times New Roman", 18, "bold")).pack(pady=10)

    Label(root, text="Name:").pack()
    entry_name = Entry(root, width=50, font=("Times New Roman", 18))
    entry_name.pack()

    Label(root, text="Email:").pack()
    entry_email = Entry(root, width=50, font=("Times New Roman", 18))
    entry_email.pack()

    Label(root, text="Password:").pack()
    entry_password = Entry(root, width=50, show="*", font=("Times New Roman", 18))
    entry_password.pack()

    Button(root, text="Register", command=handle_registration, fg="white", bg="green", font=("Times New Roman", 12)).pack(pady=20)

    # Output Label
    global label_output
    label_output = Label(root, text="", fg="green", font=("Times New Roman", 18))
    label_output.pack()
