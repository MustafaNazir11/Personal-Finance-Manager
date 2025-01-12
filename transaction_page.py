from tkinter import *
import pandas as pd
import os
from utility import centerWin, navigate_to
from tkinter import messagebox
from datetime import datetime

categories = {
    "Income": ["Income"],
    "Savings": ["Fixed Deposit", "Mutual Funds", "Stock Market", "Government Securities", "Recurring Deposits", "Others"],
    "Expenses": ["Rent", "Utilities", "Transport", "Shopping", "Others"]
}

columns = ["Date", "Category", "Subcategory", "Amount"]

def view_transaction_history(root, username):
    try:
        file_path = f"all-transaction/{username}_transactions.csv"
        if not os.path.exists(file_path):
            messagebox.showinfo("No Transactions", "No transaction history found for this user.")
            return

        transactions = pd.read_csv(file_path)

        income = transactions[transactions['Category'] == 'Income']['Amount'].sum()
        savings = transactions[transactions['Category'] == 'Savings']['Amount'].sum()
        expenses = transactions[transactions['Category'] == 'Expenses']['Amount'].sum()
        balance_amount = income - (savings + expenses)

        if expenses >= 0.1 * income:
            messagebox.showinfo("Spending Alert", "You have spent 10% or more of your income!")
        if savings >= 0.3 * income:
            messagebox.showinfo("Savings Milestone", "Congratulations! You have saved 30% or more of your income.")

        for widget in root.winfo_children():
            widget.destroy()

        Label(root, text=f"{username}'s Transaction History", font=("Helvetica", 20, "bold"), bg="#f7f9fc").pack(pady=20)

        frame = Frame(root, bg="#f7f9fc")
        frame.pack(fill=BOTH, expand=True)

        canvas = Canvas(frame, bg="#f7f9fc")
        scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="#f7f9fc")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        headers = columns
        header_frame = Frame(scrollable_frame, bg="#dce3f2")
        header_frame.pack(fill=X)
        for header in headers:
            Label(header_frame, text=header, font=("Helvetica", 12, "bold"), bg="#dce3f2", width=20).pack(side=LEFT, padx=1, pady=1)

        for _, row in transactions.iterrows():
            row_frame = Frame(scrollable_frame, bg="#f7f9fc")
            row_frame.pack(fill=X)
            for value in row:
                Label(row_frame, text=f"₹{value}" if isinstance(value, (int, float)) else value if pd.notnull(value) else "", font=("Helvetica", 12), bg="#f7f9fc", width=20, anchor="w").pack(side=LEFT, padx=1, pady=1)

        balance_label = Label(
            root,
            text=f"Balance Amount: ₹{balance_amount:.2f}",
            font=("Helvetica", 14, "bold"),
            fg="#28a745" if balance_amount > 0 else "#ff6f61",
            bg="#f7f9fc"
        )
        balance_label.pack(pady=10)

        if balance_amount <= 0:
            messagebox.showwarning("Low Balance", "Warning: Your balance is zero or negative!")

        Button(
            root,
            text="Back",
            font=("Helvetica", 14),
            command=lambda: transaction_page(root, username),
            bg="#70a1ff",
            fg="white",
            relief=RAISED
        ).pack(pady=20)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while loading the transaction history: {e}")

def transaction_page(root, username):
    centerWin(root, 500, 600)
    root.configure(bg="#f7f9fc")
    root.title("Transaction Page")

    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Transaction Page", font=("Helvetica", 22, "bold"), fg="#2c3e50", bg="#f7f9fc").pack(pady=20)
    Label(root, text=f"Welcome, {username}!", font=("Helvetica", 14), fg="#404040", bg="#f7f9fc").pack(pady=5)

    Label(root, text="Category Type:", font=("Helvetica", 14), bg="#f7f9fc").pack(pady=5)
    category_main_var = StringVar(value="Select Main Category")
    main_dropdown = OptionMenu(root, category_main_var, *categories.keys())
    main_dropdown.config(font=("Helvetica", 14), bg="#ffffff", width=25)
    main_dropdown.pack(pady=5)

    Label(root, text="Subcategory:", font=("Helvetica", 14), bg="#f7f9fc").pack(pady=5)
    subcategory_var = StringVar(value="Select Subcategory")
    sub_dropdown = OptionMenu(root, subcategory_var, "Select a Main Category First")
    sub_dropdown.config(font=("Helvetica", 14), bg="#ffffff", width=25)
    sub_dropdown.pack(pady=5)

    def update_subcategories(*args):
        main_category = category_main_var.get()
        subcategories = categories.get(main_category, [])
        menu = sub_dropdown["menu"]
        menu.delete(0, "end")
        for sub in subcategories:
            menu.add_command(label=sub, command=lambda value=sub: subcategory_var.set(value))
        subcategory_var.set("Select Subcategory")

    category_main_var.trace_add("write", update_subcategories)

    Label(root, text="Amount (₹):", font=("Helvetica", 14), bg="#f7f9fc").pack(pady=10)
    entry_amount = Entry(root, font=("Helvetica", 14), width=30)
    entry_amount.pack(pady=5)

    def add_transaction():
        main_category = category_main_var.get()
        subcategory = subcategory_var.get()
        amount = entry_amount.get()

        if main_category == "Select Main Category" or subcategory == "Select Subcategory" or not amount:
            transaction_output.config(text="Please fill out all fields.", fg="#8B0000")
            return

        try:
            amount = float(amount)
            file_name = f"all-transaction/{username}_transactions.csv"

            if os.path.exists(file_name):
                df_transaction = pd.read_csv(file_name)
            else:
                df_transaction = pd.DataFrame(columns=columns)

            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_row = {
                "Date": date,
                "Category": main_category,
                "Subcategory": subcategory,
                "Amount": amount
            }

            df_transaction = pd.concat([df_transaction, pd.DataFrame([new_row])], ignore_index=True)
            df_transaction.to_csv(file_name, index=False)
            transaction_output.config(text=f"Transaction added: {main_category} - {subcategory} - ₹{amount:.2f}", fg="#006400")

            income = df_transaction[df_transaction['Category'] == 'Income']['Amount'].sum()
            savings = df_transaction[df_transaction['Category'] == 'Savings']['Amount'].sum()
            expenses = df_transaction[df_transaction['Category'] == 'Expenses']['Amount'].sum()

            if expenses >= 0.1 * income:
                messagebox.showinfo("Spending Alert", "You have spent 10% or more of your income!")
            if savings >= 0.3 * income:
                messagebox.showinfo("Savings Milestone", "Congratulations! You have saved 30% or more of your income.")

        except ValueError:
            transaction_output.config(text="Invalid amount! Please enter a valid number.", fg="#8B0000")

    def back():
        from login import handle_login_success
        handle_login_success(root, username)

    def logout():
        from Main import main_page
        navigate_to(root, main_page)

    Button(root, text="Add Transaction", command=add_transaction, font=("Helvetica", 14, "bold"),
           bg="#70a1ff", fg="white", width=20).pack(pady=20)
    Button(
        root,
        text="Check Transaction History",
        font=("Helvetica", 14),
        command=lambda: view_transaction_history(root, username),
        bg="#75d06e",
        fg="white",
        relief=RAISED
    ).pack(pady=10)

    Button(root, text="Back", command=back, font=("Helvetica", 14, "bold"),
           bg="#70a1ff", fg="white").pack(pady=20)
    Button(root, text="Logout", command=logout, font=("Helvetica", 14, "bold"),
           bg="#70a1ff", fg="white").place(x=500, y=10, anchor="ne")

    transaction_output = Label(root, text="", font=("Helvetica", 14), bg="#f7f9fc")
    transaction_output.pack()
