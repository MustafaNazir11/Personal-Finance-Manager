from tkinter import *
import pandas as pd
import os
from utility import centerWin, navigate_to
from tkinter import messagebox

categories = {
    "Income": ["Income"],
    "Savings": ["Fixed Deposit", "Mutual Funds", "Stock Market", "Government Securities", "Recurring Deposits", "Others"],
    "Expenses": ["Rent", "Utilities", "Transport", "Shopping", "Others"]
}

columns = [f"{main}: {sub}" if sub != main else main for main in categories for sub in categories[main]]

def transaction_page(root, username):
    """Sets up the transaction page."""
    centerWin(root, 500, 600)
    root.configure(bg="#f0f0f0")
    root.title("Transaction Page")

    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Transaction Page", font=("Helvetica", 22, "bold"), fg="#000080", bg="#f0f0f0").pack(pady=20)
    Label(root, text=f"Welcome, {username}!", font=("Helvetica", 14), fg="#404040", bg="#f0f0f0").pack(pady=5)

    Label(root, text="Category Type:", font=("Helvetica", 14), bg="#f0f0f0").pack(pady=5)
    category_main_var = StringVar(value="Select Main Category")
    main_dropdown = OptionMenu(root, category_main_var, *categories.keys())
    main_dropdown.config(font=("Helvetica", 14), bg="#ffffff", width=25)
    main_dropdown.pack(pady=5)

    Label(root, text="Subcategory:", font=("Helvetica", 14), bg="#f0f0f0").pack(pady=5)
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

    category_main_var.trace("w", update_subcategories)

    Label(root, text="Amount (₹):", font=("Helvetica", 14), bg="#f0f0f0").pack(pady=10)
    entry_amount = Entry(root, font=("Helvetica", 14), width=30)
    entry_amount.pack(pady=5)

    def calculate_totals(file_name):
        if os.path.exists(file_name):
            df = pd.read_csv(file_name)
            total_income = df["Income"].sum() if "Income" in df.columns else 0
            total_savings = sum(df[col].sum() for col in df.columns if col.startswith("Savings"))
            total_shopping = df["Expenses: Shopping"].sum() if "Expenses: Shopping" in df.columns else 0
            return total_income, total_savings, total_shopping
        return 0, 0, 0

    def add_transaction():
        main_category = category_main_var.get()
        subcategory = subcategory_var.get()
        amount = entry_amount.get()

        if main_category == "Select Main Category" or subcategory == "Select Subcategory" or not amount:
            transaction_output.config(text="Please fill out all fields.", fg="#8B0000")
            return

        try:
            amount = float(amount)
            file_name = f"{username}_transactions.csv"

            if os.path.exists(file_name):
                df_transaction = pd.read_csv(file_name)
            else:
                df_transaction = pd.DataFrame(columns=columns)

            column_name = f"{main_category}: {subcategory}" if subcategory != main_category else main_category

            if column_name in df_transaction.columns:
                new_row = {col: None for col in df_transaction.columns}
                new_row[column_name] = amount
                df_transaction.dropna()
                df_transaction = pd.concat([df_transaction, pd.DataFrame([new_row])], ignore_index=True)

            df_transaction.to_csv(file_name, index=False)
            transaction_output.config(text=f"Transaction added: {main_category} - {subcategory} - ₹{amount:.2f}", fg="#006400")

            total_income, total_savings, total_shopping = calculate_totals(file_name)

            if total_shopping > total_income / 10:
                messagebox.showwarning("Shopping Alert", f"You have spent more than 10% of your income on shopping!\nIncome: ₹{total_income:.2f}\nShopping: ₹{total_shopping:.2f}")

            if total_savings >= total_income * 0.3:
                messagebox.showinfo("Savings Milestone", f"Congratulations! You have saved 30% or more of your income!\nIncome: ₹{total_income:.2f}\nSavings: ₹{total_savings:.2f}")

        except ValueError:
            transaction_output.config(text="Invalid amount! Please enter a valid number.", fg="#8B0000")

    def logout():
        from Main import main_page  # Import here to avoid circular dependency
        navigate_to(root, main_page)
    def back():
        from login import handle_login_success
        handle_login_success(root,username)

        
    Button(root, text="Add Transaction", command=add_transaction, font=("Helvetica", 14, "bold"),
           bg="#004080", fg="white", width=20).pack(pady=20)

    Button(root, text="Back", command=back, font=("Helvetica", 14, "bold"),
           bg="#004080", fg="white", width=20).pack(pady=20)
    
    Button(root, text="Logout", command= logout, font=("Helvetica", 14, "bold"),
           bg="#008080", fg="white").place(x=500, y=10, anchor="ne") 

    transaction_output = Label(root, text="", font=("Helvetica", 14), bg="#f0f0f0")
    transaction_output.pack()
