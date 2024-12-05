from tkinter import *
import pandas as pd
import os 
from datetime import datetime


categories = ["Food", "Rent", "Shopping", "Utilities", "Transport", "Others"]
df_transaction = pd.DataFrame(columns=categories)


    

def register():
    """Handles user registration."""
    global username 
    user_name = entry_name.get()
    user_email = entry_email.get()
    user_password = entry_password.get()

    username = user_email.split("@")[0]

    new_data = pd.DataFrame({
        "timestamp": [datetime.now().strftime("%d|%m|%Y %H:%M:%S")],
        "name": [user_name],
        "email": [user_email],
        "password": [user_password]
    })

    if os.path.exists("result.csv"):
        new_data.to_csv('result.csv',mode='a',index=False,header=False)
    else:
        new_data.to_csv('result.csv',mode='w',index=False,header=True)

    # Output label with a success message
    label_output.config(
        text=f"User registered successfully! Your username is '{username}'", fg="green"
    )

    # Transaction page after registration
    go_to_transaction_page()


def go_to_transaction_page():
    """Navigates to the transaction page."""
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Transaction Page", font=("Times New Roman", 18, "bold"), fg="blue").pack(pady=10)

    Label(root, text=f"Welcome, {username}!", font=("Times New Roman", 14)).pack(pady=10)

    Label(root, text="Enter Transaction Details:", font=("Times New Roman", 12)).pack(pady=10)
    df = []
    Label(root, text="Category:").pack()
    global category_var
    category_var = StringVar()
    category_var.set("Select Category") 
    dropdown = OptionMenu(root, category_var, *categories)
    dropdown.pack()

    Label(root, text="Amount:").pack()
    global entry_amount
    entry_amount = Entry(root, width=50, font=("Times New Roman", 18))
    entry_amount.pack()

    Button(root, text="Add Transaction", command=transaction, fg="white", bg="green", font=("Times New Roman", 18)).pack(pady=20)
    if os.path.exists("transaction.csv"):
        df_transaction.to_csv('transaction.csv',mode='a',index=False,header=True)
    else:
        df_transaction.to_csv('transaction.csv',mode='w',index=False,header=True)


    global transaction_output
    transaction_output = Label(root, text="", font=("Times New Roman", 18))
    transaction_output.pack()

def transaction():
    """Handles adding a transaction."""
    global df_transaction
    category = category_var.get()
    amount = entry_amount.get()

    if category != "Select Category" and amount:
        try:
            amount = float(amount)
            transaction_output.config(
                text=f"Transaction added: {category} - ₹{amount:.2f}", fg="green"
            )
            if os.path.exists("transaction.csv"):
                df_transaction = pd.read_csv("transaction.csv")
            else:
                df_transaction = pd.DataFrame(columns=categories)

            if category in df_transaction.columns:

                for col in categories:
                    new_row = {col : None}
                new_row[category] = amount
                df_transaction = pd.concat([df_transaction, pd.DataFrame([new_row])], ignore_index=True)
            else:
                df_transaction[category] = [amount]
            
            df_transaction = df_transaction.dropna(how='all')

            df_transaction.to_csv("transaction.csv", index=False)

            
        except ValueError:
            transaction_output.config(text="Invalid amount! Please enter a number.", fg="red")
    else:
        transaction_output.config(text="Please fill out all fields.", fg="red")
# Main Application
root = Tk()
root.title("PERSONAL FINANCE MANAGER")


Label(root, text="PERSONAL FINANCE TRACKER", font=("Times New Roman", 28, "bold"), fg="blue").pack(pady=20)

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

Button(root, text="Register", command=register, fg="white", bg="green", font=("Times New Roman", 12)).pack(pady=20)

# Output Label
label_output = Label(root, text="", fg="green", font=("Times New Roman", 18))
label_output.pack()

root.mainloop()
