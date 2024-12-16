from tkinter import *
import pandas as pd
import os

categories = ["Food", "Rent", "Shopping", "Utilities", "Transport", "Others"]
df_transaction = pd.DataFrame(columns=categories)

def transaction_page(root, username):
    """Sets up the transaction page."""
    # Clear the root window
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Transaction Page", font=("Times New Roman", 18, "bold"), fg="blue").pack(pady=10)
    Label(root, text=f"Welcome, {username}!", font=("Times New Roman", 14)).pack(pady=10)

    Label(root, text="Enter Transaction Details:", font=("Times New Roman", 12)).pack(pady=10)

    Label(root, text="Category:").pack()
    category_var = StringVar()
    category_var.set("Select Category")
    dropdown = OptionMenu(root, category_var, *categories)
    dropdown.pack()

    Label(root, text="Amount:").pack()
    entry_amount = Entry(root, width=50, font=("Times New Roman", 18))
    entry_amount.pack()

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
                    text=f"Transaction added: {category} - ₹{amount:.2f}", fg="green"
                )
            except ValueError:
                transaction_output.config(text="Invalid amount! Please enter a number.", fg="red")
        else:
            transaction_output.config(text="Please fill out all fields.", fg="red")

    Button(root, text="Add Transaction", command=add_transaction, fg="white", bg="green", font=("Times New Roman", 18)).pack(pady=20)
    transaction_output = Label(root, text="", font=("Times New Roman", 18))
    transaction_output.pack()
