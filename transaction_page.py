from tkinter import *
import pandas as pd
import os

categories = ["Food", "Rent", "Shopping", "Utilities", "Transport", "Others"]
df_transaction = pd.DataFrame(columns=categories)

def transaction_page(root, username):
    """Sets up the transaction page."""
    window_W, window_H = 500, 600

    screen_H = root.winfo_screenheight() #height of device (laptop,PC) screen
    screen_W = root.winfo_screenwidth()#width of device (laptop,PC) screen
    Position_V = int(screen_H/2 -window_H/2) #Vertical Position of the window
    Position_H = int(screen_W/2 - window_W/2) #Horizontal Position of the window
    root.geometry(f"{window_W}x{window_H}+{Position_H}+{Position_V}")
    # Clear the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Configure the root window
    root.configure(bg="#f0f0f0")

    # Title and welcome message
    Label(
        root,
        text="Transaction Page",
        font=("Helvetica", 22, "bold"),
        fg="#000080",
        bg="#f0f0f0"
    ).pack(pady=30)

    Label(
        root,
        text=f"Welcome, {username}!",
        font=("Helvetica", 14),
        fg="#404040",
        bg="#f0f0f0"
    ).pack(pady=10)

    Label(
        root,
        text="Enter Transaction Details:",
        font=("Helvetica", 14),
        fg="#404040",
        bg="#f0f0f0"
    ).pack(pady=15)

    # Category dropdown
    Label(
        root,
        text="Category:",
        font=("Helvetica", 14),
        fg="#404040",
        bg="#f0f0f0"
    ).pack(pady=5)

    category_var = StringVar()
    category_var.set("Select Category")
    dropdown = OptionMenu(root, category_var, *categories)
    dropdown.config(font=("Helvetica", 14), bg="#ffffff", fg="#404040", width=20)
    dropdown.pack(pady=5)

    # Amount entry
    Label(
        root,
        text="Amount:",
        font=("Helvetica", 14),
        fg="#404040",
        bg="#f0f0f0"
    ).pack(pady=10)
    entry_amount = Entry(root, width=40, font=("Helvetica", 14))
    entry_amount.pack(pady=5)

    # Add transaction function
    def add_transaction():
        """Handles adding a transaction."""
        category = category_var.get()
        amount = entry_amount.get()

        if category != "Select Category" and amount:
            try:
                amount = float(amount)
                if os.path.exists("transaction.csv"):
                    df_transaction = pd.read_csv("transaction.csv")
                else:
                    df_transaction = pd.DataFrame(columns=categories)

                if category in df_transaction.columns:
                    for col in categories:
                        new_row = {col: None}
                    new_row[category] = amount
                    df_transaction = pd.concat([df_transaction, pd.DataFrame([new_row])], ignore_index=True)
                else:
                    df_transaction[category] = [amount]

                df_transaction.dropna(how='all', inplace=True)
                df_transaction.to_csv("transaction.csv", index=False)

                transaction_output.config(
                    text=f"Transaction added: {category} - ₹{amount:.2f}", fg="#006400"
                )
            except ValueError:
                transaction_output.config(text="Invalid amount! Please enter a number.", fg="#8B0000")
        else:
            transaction_output.config(text="Please fill out all fields.", fg="#8B0000")

    # Add transaction button
    Button(
        root,
        text="Add Transaction",
        command=add_transaction,
        fg="white",
        bg="#004080",
        font=("Helvetica", 14, "bold"),
        width=18,
        height=2,
        relief="raised",
        bd=4
    ).pack(pady=25)

    # Output message
    transaction_output = Label(
        root,
        text="",
        font=("Helvetica", 14),
        fg="#8B0000",
        bg="#f0f0f0"
    )
    transaction_output.pack()
